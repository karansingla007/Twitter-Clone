# Creator: Karan Singla
# Date: 15 Oct 2022

import json

from api_base.api_base import ApiBase
from sqlite.sqlite_helper import SqliteHelper


class FeedApi(ApiBase):
    __sqliteHelperObj = SqliteHelper.instance()

    # Get user feed :- user following feed by user_name
    def __getUserFeed(self, parsed):
        selectUserIdQuery = f'''Select user_id from user where user_name = {parsed['user_name'][0]}'''
        response = self.__sqliteHelperObj.execute_select_query(selectUserIdQuery)
        y = json.loads(response)
        user_id = y[0]['user_id']
        selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from 
        userFollowing Inner Join userTweets on userFollowing.following_id = userTweets.user_id where 
        userFollowing.user_id = {user_id} '''
        response = self.__sqliteHelperObj.execute_select_query(selectUserTweetsQuery)
        return response

    # Handle rotes of feed get api
    def handleGetFeedQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}

        if '/feed/by/userName' in path:
            response = self.__getUserFeed(parsed)

        if server is None:
            return response
        else:
            super().return_success_response(response, server)
