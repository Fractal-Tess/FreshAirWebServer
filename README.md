How to build an executable :

python ver = 3.6.8
pyinstaller  --hidden-import pkg_resources --hidden-import infi.systray --noconsole --onefile --icon=icon.ico main.py