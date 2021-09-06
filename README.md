FreshAirWebServer that can be compiled to an executable via pyinstaller for distribution.

This repo serves the purpose of combining FreshAirWeb with a simple python web server for easy distributed deployment.


How to build an executable :

Working & tested python versions:
ver==3.8.8

pyinstaller  --hidden-import pkg_resources --hidden-import infi.systray --noconsole --onefile --icon=icon.ico main.py