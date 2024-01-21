import main
import subprocess
import time
version = main.__version__.replace('v', '')
year = time.strftime("%Y")
if not year == "2024":
    year = "2024-" + year


subprocess.check_call(
    [
        "python", "-m", "nuitka",
        "--onefile",
        "--standalone",
        "--follow-imports",
        "--lto=yes",
        "--report=report.xml",
        "--mingw64",
        "--show-progress",
        "--show-memory",
        "--windows-disable-console",
        "--enable-plugin=pyside6",
        "--windows-icon-from-ico=resource\\icon\\logo.png",
        "--output-dir=output",
        "--output-filename=抽签.exe",
        "--product-name=抽签",
        "--product-version=" + version,
        f"--copyright=Copyright (C) {year}  沉默の金",
        "main.py"
    ]
)
