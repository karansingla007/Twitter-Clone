from http.server import HTTPServer, BaseHTTPRequestHandler

from end_point_handler.feed import handleGetFeedQuery
from end_point_handler.tweet import handleGetTweetQuery, handlePostTweetQuery
from end_point_handler.users import handlePostUserQuery, handleGetUserQuery

# HOST = "ec2-15-207-87-184.ap-south-1.compute.amazonaws.com"
# PORT = 8080

HOST = "localhost"
PORT = 8000


class MyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/user/' in self.path:
            handleGetUserQuery(self)
        elif '/tweet' in self.path:
            handleGetTweetQuery(self)
        elif '/feed' in self.path:
            handleGetFeedQuery(self)

    def do_POST(self):
        if '/user/' in self.path:
            handlePostUserQuery(self)
        elif '/tweet' in self.path:
            handlePostTweetQuery(self)


server = HTTPServer((HOST, PORT), MyHTTP)
print("server running now....")
server.serve_forever()
server.server_close()
print("server closed now....")
