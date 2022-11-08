# Creator: Karan Singla
# Date: 20 Oct 2022

from api_base.api_base import ApiBase
from sqlite.sqlite_helper import SqliteHelper
from twitter_api.api_client import fetchTwitterUserDetailByUserName

sqliteHelperObj = SqliteHelper.instance()


class UsersApi(ApiBase):
    # get all users list
    def __getAllUsersDetails(self):
        selectUserDetailQuery = '''Select user_id, name, user_name, bio from user'''
        response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

        return response

    # get particular userId
    def __getUsersDetails(self, parsed):
        selectUserDetailQuery = f'''Select user_id, name, user_name, bio from user where user_id = {parsed['user_id'][0]}'''
        response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

        return response

    # get user followers list
    def __getUserFollowerList(self, parsed):
        selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollower on 
        user.user_id = userFollower.follower_id where userFollower.user_id = {parsed['user_id'][0]} '''
        response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

        return response

    # get user following list
    def __getUserFollowingList(self, parsed):
        selectUserDetailQuery = f'''Select user.name, user.user_name, user.bio from user Inner Join userFollowing on 
        user.user_id = userFollowing.following_id where userFollowing.user_id = {parsed['user_id'][0]} '''
        response = sqliteHelperObj.execute_select_query(selectUserDetailQuery)

        return response

    # post Apis
    # fetch detail from twitter and store in db
    def __getAndStoreUserDetail(self, parsed):
        # json_response = fetchTwitterUserDetailByUserName(f"usernames={parsed['twitter_user_name'][0]}")
        json_response = fetchTwitterUserDetailByUserName(
            "usernames=karansinglaOO7,saurabhs679,karafrenor,kartikryder,thegambhirjr7,sdrth,karannagpal96,"
            "anshulgoel02,CAPalakSingla2,theguywithideas")
        for x in json_response['data']:
            insertUserDetailQuery = '''Insert into user(user_id, name, user_name, bio) values (%s, %s, %s, %s)''' % (
                "'" + x['id'] + "'", "'" + x['name'] + "'", "'" + x['username'] + "'", "'" + x['description'] + "'")
            sqliteHelperObj.execute_insert_query(insertUserDetailQuery)

        response = {'response': 200}
        return response

    # follow any user
    def __userFollow(self, parsed):
        insertUserFollowerQuery = f'''Insert into userFollower(user_id, follower_id) values ({parsed['following_id'][0]}, {parsed['user_id'][0]})'''
        insertUserFollowingQuery = f'''Insert into userFollowing(user_id, following_id) values ({parsed['user_id'][0]}, {parsed['following_id'][0]})'''

        sqliteHelperObj.execute_insert_query(insertUserFollowerQuery)
        sqliteHelperObj.execute_insert_query(insertUserFollowingQuery)

        response = {'response': 200}
        return response

    # unfollow any user
    def __userUnfollow(self, parsed):
        deleteUserFollowerQuery = f'''Delete from userFollower where user_id = {parsed['following_id'][0]} AND 
        follower_id = {parsed['user_id'][0]}'''
        deleteUserFollowingQuery = f'''Delete from userFollowing where user_id = {parsed['user_id'][0]} AND following_id = {parsed['following_id'][0]}'''
        sqliteHelperObj.execute_insert_query(deleteUserFollowerQuery)
        sqliteHelperObj.execute_insert_query(deleteUserFollowingQuery)

        response = {'response': 200}
        return response

    # Perform get operations on user

    def handleGetUserQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}
        if path == '/user/all/details':
            response = self.__getAllUsersDetails()
        elif '/user/details' in path:
            response = self.__getUsersDetails(parsed)
        elif '/user/followers' in path:
            response = self.__getUserFollowerList(parsed)
        elif '/user/following' in path:
            response = self.__getUserFollowingList(parsed)

        if server is None:
            return response
        else:
            super().return_success_response(response, server)

    # Perform create, update, delete operations on user
    def handlePostUserQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}
        if '/user/follow' in path:
            response = self.__userFollow(parsed)
        elif '/user/unfollow' in path:
            response = self.__userUnfollow(parsed)
        elif '/user/add' in path:
            response = self.__getAndStoreUserDetail(parsed)

        super().return_success_response(response, server)
