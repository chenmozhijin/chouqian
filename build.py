import main
import subprocess
version = main.__version__.replace('v', '')

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
        "--copyright=沉默の金",
        "main.py"
    ]
)
