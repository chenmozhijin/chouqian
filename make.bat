python -m nuitka --onefile --standalone --follow-imports --lto=no --report=report.xml --mingw64 --show-progress --show-memory --windows-disable-console --enable-plugin=pyside6 --windows-icon-from-ico="resource\icon\logo.png" --output-dir=output main.py