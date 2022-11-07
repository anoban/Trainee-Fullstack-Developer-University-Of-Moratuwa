# this is a dummy Python web server :)
# HTTPServer for define a web server
# BaseHTTPRequestHandler to handle user inputs & show web pages

from http.server import HTTPServer, BaseHTTPRequestHandler

# a class to handle user requests!
class WebServer(BaseHTTPRequestHandler):
    # do_GET() is a pre-defined but customizeable method in the module, not a user defined one!!!!!
    def do_GET(self):
        self.path = "D:/UoM/Server Side Web Programming/index.html"

        # read in the html file
        file = open(self.path, "r").read()

        # to send a status update to client
        self.send_response(200)

        # ending the request headers!, to be followed by the content.
        self.end_headers()
        
        # sending the file to client, encode the read file as utf-8 bytes and send it to client
        self.wfile.write(bytes(file, "utf-8"))

# defining a server
myServer = HTTPServer(("localhost", 1997), WebServer)
myServer.serve_forever()

