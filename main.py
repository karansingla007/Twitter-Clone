from http.server import HTTPServer, BaseHTTPRequestHandler

from api_base.end_point_handler.feed_api import FeedApi
from api_base.end_point_handler.users_api import UsersApi
from api_base.end_point_handler.tweet_api import TweetApi

# HOST = "ec2-15-207-87-184.ap-south-1.compute.amazonaws.com"
# PORT = 8080

HOST = "localhost"
PORT = 8000


class MyHTTP(BaseHTTPRequestHandler):
    feedApi = FeedApi()
    usersApi = UsersApi()
    tweetApi = TweetApi()

    def do_GET(self):
        if '/user/' in self.path:
            self.usersApi.handleGetUserQuery(self.path, self)
        elif '/tweet' in self.path:
            self.tweetApi.handleGetTweetQuery(self.path, self)
        elif '/feed' in self.path:
            self.feedApi.handleGetFeedQuery(self.path, self)

    def do_POST(self):
        if '/user/' in self.path:
            self.usersApi.handlePostUserQuery(self.path, self)
        elif '/tweet' in self.path:
            self.tweetApi.handlePostTweetQuery(self.path, self)


server = HTTPServer((HOST, PORT), MyHTTP)
print("server running now....")
server.serve_forever()
server.server_close()
print("server closed now....")
