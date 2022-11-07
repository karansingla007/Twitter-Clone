import json

from end_point_handler.response import returnSuccessResponse
from urllib.parse import urlparse, parse_qs
from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper.instance()


def getUserFeed(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    selectUserIdQuery = f'''Select user_id from user where user_name = {parsed['user_name'][0]}'''
    response = sqliteHelperObj.execute_select_query(selectUserIdQuery)
    y = json.loads(response)
    user_id = y[0]['user_id']
    selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from
    userFollowing Inner Join userTweets on userFollowing.following_id = userTweets.user_id where userFollowing.user_id = {user_id}'''

    print('###########')
    print(selectUserTweetsQuery)

    response = sqliteHelperObj.execute_select_query(selectUserTweetsQuery)

    returnSuccessResponse(self, response)


def handleGetFeedQuery(self):
    if '/feed/by/userName' in self.path:
        getUserFeed(self)
