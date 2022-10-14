import json
from urllib.parse import urlparse, parse_qs

from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper()

def getAllUsersDetails(self):
    sqliteHelperObj.useDatabaseQuery()
    selectUserDetailQuery = '''Select user_id, name, user_name, bio from user'''
    response = sqliteHelperObj.executeSelectQuery(selectUserDetailQuery)

    self.send_response(200, response)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(str(response), "utf-8"))

def getUserFollower(self):
    print("########")
    parsed = parse_qs(urlparse(self.path).query)
    print(parsed["abc"])
    # print(query_string.split('&'))
    # sqliteHelperObj.useDatabaseQuery()
    # selectUserDetailQuery = '''Select * from userFollower'''
    # response = sqliteHelperObj.executeSelectQuery(selectUserDetailQuery)

    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    # self.wfile.write(bytes(str(response), "utf-8"))

def getUserFollowing(self):
    sqliteHelperObj.useDatabaseQuery()
    selectUserDetailQuery = '''Select * from userFollowing'''
    response = sqliteHelperObj.executeSelectQuery(selectUserDetailQuery)

    self.send_response(200, response)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(str(response), "utf-8"))


def handleUserQuery(self):
    if self.path == '/user/all/details':
        getAllUsersDetails(self)
    elif '/user/followers' in self.path:
        getUserFollower(self)
    elif self.path == '/user/following':
        getUserFollowing(self)