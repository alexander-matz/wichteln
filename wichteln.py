#!/usr/bin/env python3

import requests

import time
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from pprint import pprint
from base64 import b64decode

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'html')
        if self.path == '/':
            filename = root + '/index.html'
        else:
            filename = root + self.path

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)

    def do_POST(self):
        if self.path != '/send':
            self.send_response_only(404)
            return
        request_body = self.rfile.read(int(self.headers.get('Content-Length')))
        request_json = json.loads(request_body)
        auth_header = self.headers.get("Authorization")
        if not auth_header.startswith("Basic "):
            self.send_response_only(400)
            return

        auth_data = b64decode(auth_header.lstrip("Basic ")).decode()
        account, key = auth_data.split(":", 2)
        response = requests.post(
            "https://api.mailjet.com/v3.1/send",
            auth = (account, key),
            json = request_json,
        )
        pprint(json.loads(response.text))
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.text.encode())


HOST_NAME = 'localhost'
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s/' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s/' % (HOST_NAME, PORT_NUMBER))
