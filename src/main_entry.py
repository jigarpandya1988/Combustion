"""
Commercial-grade PLC Monitoring Framework

Modules:
- PLCCommunication: Handles polling and tag change detection (async/threaded for high-volume tags)
- SQLiteLogger: Logs data to SQLite database (concurrent-safe)
- JSONLogger: Handles JSON rolling logging
- CSVExporter: Exports historical tag data to CSV

Usage:
- Import and instantiate each class separately
- Designed for concurrent execution via asyncio or threads
- Extend or integrate into a controller class

Assumptions:
- pycomm3 supports Logix PLCs (ControlLogix, CompactLogix)
- Tags must be controller-scoped and valid
- Required Python >= 3.9
"""

import asyncio
import json
import logging
import multiprocessing
import os

from plc.rockwell.logix import PLCCommunication
from sqlitex.sqlite_logger import SQLiteLogger
from utils.csv_utils.csv_logger import CSVExporter
from utils.json_utils.json_logger import JSONLogger


def setup_logging(config):
    level = getattr(logging, config["level"].upper(), logging.INFO)
    os.makedirs(os.path.dirname(config["file"]), exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler(config["file"]), logging.StreamHandler()],
    )


def plc_worker(plc_config: dict):
    """
    Process-safe PLC polling worker. Sets up communication and loggers.
    """
    ip = plc_config["ip"]
    tags = plc_config["tags"]
    poll_interval = plc_config.get("poll_interval", 1.0)

    logger = SQLiteLogger(plc_config["sqlite_path"])
    json_logger = JSONLogger(plc_config["json_path"])
    csv_exporter = CSVExporter(plc_config["sqlite_path"])

    export_trigger_tag = plc_config.get("export_trigger_tag")
    export_csv_path = plc_config.get("csv_path")
    export_minutes = plc_config.get("export_minutes")

    last_trigger = "false"

    def handle_changes(changes):
        nonlocal last_trigger
        logger.log(changes)
        json_logger.append(changes)

        # Check trigger tag for CSV export
        for tag, val in changes:
            if tag == export_trigger_tag:
                if last_trigger == "false" and val == "true":
                    logging.info(f"[{ip}] Triggered export → {export_csv_path}")
                    csv_exporter.export(export_csv_path, export_minutes)
                last_trigger = val

    async def run():
        comm = PLCCommunication(ip, tags, poll_interval)
        await comm.start_polling(handle_changes)

    asyncio.run(run())


def main():
    with open("config.json") as f:
        config = json.load(f)

    setup_logging(config["logging"])

    processes = []
    for plc_config in config["plcs"]:
        p = multiprocessing.Process(target=plc_worker, args=(plc_config,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    multiprocessing.freeze_support()  # Windows-safe
    main()
