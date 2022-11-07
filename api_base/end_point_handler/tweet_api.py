from api_base.api_base import ApiBase
from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper.instance()


class TweetApi(ApiBase):
    def createTweet(self, parsed):
        createTweetQuery = f'''Insert into userTweets(user_id, title, description) values ({parsed['user_id'][0]}, {parsed['title'][0]}, {parsed['description'][0]})'''
        sqliteHelperObj.execute_insert_query(createTweetQuery)

        response = {'response': 200, 'status': 'created'}
        return response


    def deleteTweet(self, parsed):
        createTweetQuery = f'''Delete from userTweets where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        response = {'response': 200, 'status': 'deleted'}
        return response


    def editTweet(self, parsed):
        createTweetQuery = f'''Update userTweets set title = {parsed['title'][0]}, description = {parsed['description'][0]} where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        response = {'response': 200, 'status': 'deleted'}
        return response


    def getTweetsFromUser(self, parsed):
        selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from user Inner Join userTweets on user.user_id = userTweets.user_id where user.user_name = {parsed['user_name'][0]}'''

        response = sqliteHelperObj.execute_select_query(selectUserTweetsQuery)
        return response

    def handleGetTweetQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}

        if '/tweet/list/by/userName' in path:
            response = self.getTweetsFromUser(parsed)
        super().return_success_response(response, server)


    def handlePostTweetQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}
        if '/tweet/create' in path:
            response = self.createTweet(parsed)
        elif '/tweet/delete' in path:
            response = self.deleteTweet(parsed)
        elif '/tweet/edit' in path:
            response = self.editTweet(parsed)
        super().return_success_response(response, server)
