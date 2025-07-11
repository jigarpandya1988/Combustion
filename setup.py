from setuptools import find_packages, setup


def read_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()


setup(
    name="Combustion",  # 🔁 Change this
    version="0.1.0",  # 🔁 Use semantic versioning
    author="JigarPandya",
    author_email="ultijigar@gmail.com",
    description="Industrial Automation",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/jigarpandya1988/Combustion",  # 🔁 GitHub/project URL
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",  # 🔁 Update if you use different license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
