from urllib.parse import urlparse, parse_qs

from end_point_handler.response import returnSuccessResponse
from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper()


# get all end_point_handler list
def getAllUsersDetails(self):
    sqliteHelperObj.use_database_query()
    selectUserDetailQuery = '''Select user_id, name, user_name, bio from user'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    returnSuccessResponse(self, response)


# get particular userId
def getUsersDetails(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)

    selectUserDetailQuery = f'''Select user_id, name, user_name, bio from user where user_id = {parsed['user_id'][0]}'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    returnSuccessResponse(self, response)


# get user followers
def getUserFollowerList(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollower on user.user_id = userFollower.follower_id where userFollower.user_id = {parsed['user_id'][0]}'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    returnSuccessResponse(self, response)


# get user following
def getUserFollowingList(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollowing on user.user_id = userFollowing.following_id where userFollowing.user_id = {parsed['user_id'][0]}'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    returnSuccessResponse(self, response)


# post Apis
def userFollow(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    insertUserFollowerQuery = f'''Insert into userFollower(user_id, follower_id) values ({parsed['following_id'][0]}, {parsed['user_id'][0]})'''
    insertUserFollowingQuery = f'''Insert into userFollowing(user_id, following_id) values ({parsed['user_id'][0]}, {parsed['following_id'][0]})'''

    sqliteHelperObj.execute_insert_query(insertUserFollowerQuery)
    sqliteHelperObj.execute_insert_query(insertUserFollowingQuery)

    response = {'response': 200}
    returnSuccessResponse(self, response)


def userUnfollow(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    deleteUserFollowerQuery = f'''Delete from userFollower where user_id = {parsed['following_id'][0]} AND 
    follower_id = {parsed['user_id'][0]}'''
    deleteUserFollowingQuery = f'''Delete from userFollowing where user_id = {parsed['user_id'][0]} AND following_id = {parsed['following_id'][0]}'''
    sqliteHelperObj.execute_insert_query(deleteUserFollowerQuery)
    sqliteHelperObj.execute_insert_query(deleteUserFollowingQuery)

    response = {'response': 200}
    returnSuccessResponse(self, response)

# Perform get operations on user
def handleGetUserQuery(self):
    if self.path == '/user/all/details':
        getAllUsersDetails(self)
    elif '/user/details' in self.path:
        getUsersDetails(self)
    elif '/user/followers' in self.path:
        getUserFollowerList(self)
    elif '/user/following' in self.path:
        getUserFollowingList(self)


def handlePostUserQuery(self):
    if '/user/follow' in self.path:
        userFollow(self)
    elif '/user/unfollow' in self.path:
        userUnfollow(self)
