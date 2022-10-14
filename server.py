from http.server import HTTPServer, BaseHTTPRequestHandler
from users.users import handleUserQuery

HOST = "172.31.44.52"
PORT = 22


class MyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/user' in self.path:
            handleUserQuery(self)
        # elif '/user' in self.path:
        #     handleUserQuery(self)

    def do_POST(self):
        if self.path == '/user/get/all':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

server = HTTPServer((HOST, PORT), MyHTTP)
print("server running now....")
server.serve_forever()
server.server_close()