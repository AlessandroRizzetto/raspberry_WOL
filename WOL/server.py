#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        return
    def do_POST(self):
        self.send_response(200)
        text = self.rfile.read(int(self.headers['Content-Length']))
        print(text.decode('utf-8'))
        os.path.dirname(os.path.abspath(__file__))
        esecuzione = os.popen('./wakeon.sh {0}'.format(text.decode('utf-8'))).read()
        print(esecuzione)
        return

if __name__ == '__main__':
# Creiamo un oggetto HTTPServer che ascolterà sulla porta 9000
    server = HTTPServer(('192.168.1.69', 9000), MyServer)
    print('Server in esecuzione...')
# Avvio server
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
