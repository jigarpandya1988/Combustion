# Combustion
Industrial Automation

# 🔥 Combustion

**Combustion** is an industrial automation framework built in Python. It is designed for real-time PLC tag monitoring, data logging, and scalable system design with code modularity in mind. The project integrates logging to SQLite and JSON, supports multi-tag communication (Rockwell PLCs), and is structured for production use with pre-commit hooks and CI/CD support.

---

## ⚙️ Features

- ✅ Real-time tag monitoring and logging
- ✅ Built-in support for Allen-Bradley (Rockwell) Logix PLCs
- ✅ Modular design: `plc/`, `utils/`, `sqlitex/`, `config.json`
- ✅ Logging to:
  - `.csv`
  - `.json`
  - `.sqlite3`
- ✅ Structured for 40K+ tags, multiprocessing-ready
- ✅ Auto-formatting with Black + Isort + Flake8
- ✅ GitHub Actions workflow for automated CI/CD
- ✅ Pre-commit hooks to enforce code quality
- ✅ Built-in build system via `setup.py` and `build`

---

## 🗂 Project Structure

```text
Combustion/
├── src/
│   ├── plc/               # PLC-specific logic (e.g., Rockwell)
│   ├── sqlitex/           # SQLite logging logic
│   ├── utils/             # JSON, export, and helper utilities
│   └── config.json        # PLC and tag config
├── .github/workflows/     # GitHub Actions CI pipeline
│   └── release.yml
├── .pre-commit-config.yaml # Code formatting + linting rules
├── .flake8                 # Flake8 config
├── requirements.txt        # Python dependencies
├── setup.py                # Build config
├── pyproject.toml          # Modern tool config
├── format_and_build.bat    # One-click format + build script
└── README.md               # You're here!

```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/jigarpandya1988/Combustion.git
cd Combustion
```

### 2. Install Dependencies
```chatinput
pip install -r requirements.txt

Or using a virtual environment:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Project
```chatinput
python src/main_entry.py
```

## 🧪 Development & Testing
### Run All Formatting, Linting, and Build
```chatinput
format_and_build.bat
```

### Manually Format and Lint
```chatinput
black .
isort .
flake8 .
```

## 🛠 Build the Package
```chatinput
python -m build
```
Distributions are saved to the dist/ folder.

## 🔁 Pre-Commit Hooks
To install pre-commit hooks (run formatting/lint before every commit):
```chatinput
pip install pre-commit
pre-commit install
```
To run on all files:
```chatinput
pre-commit run --all-files
```

## 🔄 GitHub Actions CI/CD
GitHub Actions workflow (.github/workflows/release.yml) will:

Auto-format code with black and isort

Lint with flake8

Build your package

Trigger only on:

Pushes to tags like v1.0.0

Pushes to release/* branches

## 📜 License

This software is proprietary and protected by copyright.

You may not use, copy, modify, or redistribute any part of this code without explicit written permission.

To request special access or a commercial license, contact:
📧 [ultijigar@gmail.com](mailto:ultijigar@gmail.com)

⚠️ **Disclaimer:** This software is not certified for use in industrial control, automation, or safety-critical systems. Use at your own risk.


## 🙌 Credits
Developed and maintained by `Jigar Pandya`

Built with ❤️ for scalable industrial automation.


---

Let me know if you want:
- A simplified or multilingual version
- A `README.dev.md` version for contributors only
- This injected into your repo automatically with a script
