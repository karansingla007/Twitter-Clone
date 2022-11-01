from end_point_handler.response import returnSuccessResponse
from urllib.parse import urlparse, parse_qs
from sqlite.sqlite_helper import SqliteHelper

sqliteHelperObj = SqliteHelper()


def createTweet(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    createTweetQuery = f'''Insert into userTweets(user_id, title, description) values ({parsed['user_id'][0]}, {parsed['title'][0]}, {parsed['description'][0]})'''
    sqliteHelperObj.execute_insert_query(createTweetQuery)

    response = {'response': 200, 'status': 'created'}
    returnSuccessResponse(self, response)


def deleteTweet(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    createTweetQuery = f'''Delete from userTweets where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
    sqliteHelperObj.execute_query(createTweetQuery)

    response = {'response': 200, 'status': 'deleted'}
    returnSuccessResponse(self, response)


def editTweet(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    createTweetQuery = f'''Update userTweets set title = {parsed['title'][0]}, description = {parsed['description'][0]} where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
    sqliteHelperObj.execute_query(createTweetQuery)

    response = {'response': 200, 'status': 'deleted'}
    returnSuccessResponse(self, response)


def getTweetsFromUser(self):
    sqliteHelperObj.use_database_query()
    parsed = parse_qs(urlparse(self.path).query)
    selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from user Inner Join userTweets on user.user_id = userTweets.user_id where user.user_name = {parsed['user_name'][0]}'''

    response = sqliteHelperObj.execute_select_query(selectUserTweetsQuery)
    returnSuccessResponse(self, response)


def handleGetTweetQuery(self):
    if '/tweet/list/by/userName' in self.path:
        getTweetsFromUser(self)


def handlePostTweetQuery(self):
    if '/tweet/create' in self.path:
        createTweet(self)
    elif '/tweet/delete' in self.path:
        deleteTweet(self)
    elif '/tweet/edit' in self.path:
        editTweet(self)
