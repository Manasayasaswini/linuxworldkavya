import http.server
import socketserver
import os
from urllib.parse import quote
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
DIRECTORY = "."   # Change to any folder you want to serve

class FileServerHandler(SimpleHTTPRequestHandler):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, directory=DIRECTORY, **kwargs)

def run_server():
    # Get local server URL
    server_url = f"http://localhost:{PORT}"
    print("\n==============================")
    print("   Simple File Transfer Server")
    print("==============================")
    print(f" Serving Directory : {os.path.abspath(DIRECTORY)}")
    print(f" URL               : {server_url}")
    print(" Press CTRL+C to stop the server")
    print("==============================\n")

    try:
        with ThreadingHTTPServer(("", PORT), FileServerHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer Stopped Successfully!")

if _name_ == "_main_":
    run_server()
