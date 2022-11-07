from urllib.parse import urlparse, parse_qs

from end_point_handler.response import returnSuccessResponse
from sqlite.sqlite_helper import SqliteHelper
from twitter_api.api_client import fetchTwitterUserDetailByUserName

sqliteHelperObj = SqliteHelper.instance()


# get all end_point_handler list
def getAllUsersDetails():
    selectUserDetailQuery = '''Select user_id, name, user_name, bio from user'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    return response


# get particular userId
def getUsersDetails(parsed):
    selectUserDetailQuery = f'''Select user_id, name, user_name, bio from user where user_id = {parsed['user_id'][0]}'''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    return response


# get user followers
def getUserFollowerList(parsed):
    selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollower on 
    user.user_id = userFollower.follower_id where userFollower.user_id = {parsed['user_id'][0]} '''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    return response


# get user following
def getUserFollowingList(parsed):
    selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollowing on 
    user.user_id = userFollowing.following_id where userFollowing.user_id = {parsed['user_id'][0]} '''
    response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

    return response


# post Apis
def getAndStoreUserDetail(parsed):
    json_response = fetchTwitterUserDetailByUserName(f"usernames={parsed['twitter_user_name']}")
    for x in json_response['data']:
        insertUserDetailQuery = '''Insert into user(user_id, name, user_name, bio) values (%s, %s, %s, %s)''' % (
            "'" + x['id'] + "'", "'" + x['name'] + "'", "'" + x['username'] + "'", "'" + x['description'] + "'")
        sqliteHelperObj.executeInsertQuery(insertUserDetailQuery)

    response = {'response': 200}
    return response


def userFollow(parsed):
    insertUserFollowerQuery = f'''Insert into userFollower(user_id, follower_id) values ({parsed['following_id'][0]}, {parsed['user_id'][0]})'''
    insertUserFollowingQuery = f'''Insert into userFollowing(user_id, following_id) values ({parsed['user_id'][0]}, {parsed['following_id'][0]})'''

    sqliteHelperObj.execute_insert_query(insertUserFollowerQuery)
    sqliteHelperObj.execute_insert_query(insertUserFollowingQuery)

    response = {'response': 200}
    return response


def userUnfollow(parsed):
    deleteUserFollowerQuery = f'''Delete from userFollower where user_id = {parsed['following_id'][0]} AND 
    follower_id = {parsed['user_id'][0]}'''
    deleteUserFollowingQuery = f'''Delete from userFollowing where user_id = {parsed['user_id'][0]} AND following_id = {parsed['following_id'][0]}'''
    sqliteHelperObj.execute_insert_query(deleteUserFollowerQuery)
    sqliteHelperObj.execute_insert_query(deleteUserFollowingQuery)

    response = {'response': 200}
    return response


# Perform get operations on user
def handleGetUserQuery(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    response = {}

    if self.path == '/user/all/details':
        response = getAllUsersDetails()
    elif '/user/details' in self.path:
        response = getUsersDetails(parsed)
    elif '/user/followers' in self.path:
        response = getUserFollowerList(parsed)
    elif '/user/following' in self.path:
        response = getUserFollowingList(parsed)
    returnSuccessResponse(self, response)


def handlePostUserQuery(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    response = {}
    if '/user/follow' in self.path:
        response = userFollow(parsed)
    elif '/user/unfollow' in self.path:
        response = userUnfollow(parsed)
    elif '/user/add' in self.path:
        response = getAndStoreUserDetail(parsed)

    returnSuccessResponse(self, response)
