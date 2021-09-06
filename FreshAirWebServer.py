import http.server 
import socketserver
from infi.systray import SysTrayIcon
import os
import signal
import time


def on_quit_callback(_):
    print("shutdown")
    # TODO: Find a proper way to close the app and the tray icon
    os.kill(os.getpid(), signal.SIGTERM)
    
systray = SysTrayIcon("icon.ico", "Example tray icon", on_quit=on_quit_callback)
systray.start()

hostName = "localhost"
serverPort = 8000


class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path="FreshAirWeb/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":        
    webServer = socketserver.TCPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        on_quit_callback(systray)
        pass

    webServer.server_close()
    print("Server stopped.")
