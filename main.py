from http.server import HTTPServer, BaseHTTPRequestHandler
from users.users import handleUserQuery

from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper()
# HOST = "ec2-15-207-87-184.ap-south-1.compute.amazonaws.com"
# PORT = 8080

HOST = "localhost"
PORT = 8000


# def getAndStoreUserDetail():
    # json_response = fetchTwitterUserDetailByUserName("usernames=karansinglaOO7,saurabhs679,karafrenor,kartikryder,thegambhirjr7,sdrth,karannagpal96,anshulgoel02,CAPalakSingla2,theguywithideas")
    # print(json_response)
    # for x in json_response['data']:
    #     insertUserDetailQuery = '''Insert into user(user_id, name, user_name, bio) values (%s, %s, %s, %s)'''%("'"+x['id']+"'","'"+x['name']+"'", "'"+x['username']+"'", "'"+x['description']+"'")
    #     sqliteHelperObj.executeInsertQuery(insertUserDetailQuery)


class MyHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/user' in self.path:
            handleUserQuery(self)
        # elif '/user' in self.path:
        #     handleUserQuery(self)

    def do_POST(self):
        if '/user' in self.path:
            handleUserQuery(self)


server = HTTPServer((HOST, PORT), MyHTTP)
print("server running now....")
server.serve_forever()
server.server_close()
print("server closed now....")
