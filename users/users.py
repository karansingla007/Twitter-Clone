import json
from urllib.parse import urlparse, parse_qs

from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper()

# get all users list
def getAllUsersDetails(self):
    sqliteHelperObj.use_database_query()
    selectUserDetailQuery = '''Select user_id, name, user_name, bio from user'''
    response = sqliteHelperObj.use_database_query(selectUserDetailQuery)

    self.send_response(200, response)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(str(response), "utf-8"))

# get user followers
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

# get user following
def getUserFollowing(self):
    sqliteHelperObj.use_database_query()
    selectUserDetailQuery = '''Select * from userFollowing'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    self.send_response(200, response)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(str(response), "utf-8"))


# Perform get operations on user
def handleUserQuery(self):
    if self.path == '/user/all/details':
        getAllUsersDetails(self)
    elif '/user/followers' in self.path:
        getUserFollower(self)
    elif self.path == '/user/following':
        getUserFollowing(self)