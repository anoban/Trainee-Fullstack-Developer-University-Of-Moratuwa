from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path = "D:/UoM/Server Side Web Programming/node-proj/dummy.json"
        file = json.read(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.writable(bytes(file, "utf-8"))

server = HTTPServer(("0.0.0.0", 1101), web_server)
server.serve_forever()
