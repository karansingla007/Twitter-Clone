from api_base.api_base import ApiBase
from sqlite.sqlite_helper import SqliteHelper
import json
sqliteHelperObj = SqliteHelper.instance()


class TweetApi(ApiBase):
    def __createTweet(self, parsed):
        createTweetQuery = f'''Insert into userTweets(user_id, title, description) values ({parsed['user_id'][0]}, {parsed['title'][0]}, {parsed['description'][0]})'''
        sqliteHelperObj.execute_insert_query(createTweetQuery)

        response = {'response': 200, 'status': 'created'}
        return response

    def __deleteTweet(self, parsed):
        createTweetQuery = f'''Delete from userTweets where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        response = {'response': 200, 'status': 'deleted'}
        return response

    def __editTweet(self, parsed):
        createTweetQuery = f'''Update userTweets set title = {parsed['title'][0]}, description = {parsed['description'][0]} where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        response = {'response': 200, 'status': 'edited'}
        return response

    def __getTweetsFromUser(self, parsed):
        selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from user Inner Join userTweets on user.user_id = userTweets.user_id where user.user_name = {parsed['user_name'][0]}'''

        response = sqliteHelperObj.execute_select_query(selectUserTweetsQuery)
        return response

    def __getTweetsLikedUserList(self, parsed):
        selectLikedTweetsQuery = f'''Select user.user_id, user.user_name, user.name, user.bio from user Inner Join userLikes on user.user_id = userLikes.user_id where userLikes.tweet_id = {parsed['tweet_id'][0]} And userLikes.status = 0'''
        response = sqliteHelperObj.execute_select_query(selectLikedTweetsQuery)
        return response

    def __likeTweet(self, parsed):
        checkLikeQuery = f'''select status from userLikes where user_id = {parsed['user_id'][0]}  and tweet_id = {parsed['tweet_id'][0]}'''
        checkLike = sqliteHelperObj.execute_select_query(checkLikeQuery)
        json_object = json.loads(checkLike)
        if len(json_object) > 0 and json_object[0]['status'] == 0:
            response = {'response': 400, 'status': 'Already liked tweet'}
        else:
            createLikeQuery = f'''Insert into userLikes(user_id, tweet_id, status) values ({parsed['user_id'][0]}, {parsed['tweet_id'][0]}, 0)'''
            sqliteHelperObj.execute_insert_query(createLikeQuery)
            response = {'response': 200, 'status': 'Liked tweet'}
        return response

    def __dislikeTweet(self, parsed):

        checkDislikeQuery = f'''select status from userLikes where user_id = {parsed['user_id'][0]} and tweet_id = {parsed['tweet_id'][0]}'''
        checkDislike = sqliteHelperObj.execute_select_query(checkDislikeQuery)
        json_object = json.loads(checkDislike)
        if len(json_object) > 0 and json_object[0]['status'] == 1:
            response = {'response': 400, 'status': 'Already disliked tweet'}
        else:
            createDislikeQuery = f'''Insert into userLikes(user_id, tweet_id, status) values ({parsed['user_id'][0]}, {parsed['tweet_id'][0]}, 1)'''
            sqliteHelperObj.execute_insert_query(createDislikeQuery)
            response = {'response': 200, 'status': 'Disliked tweet'}
        return response


    def handleGetTweetQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}

        if '/tweet/list/by/userName' in path:
            response = self.__getTweetsFromUser(parsed)
        elif 'tweet/like/list' in path:
            response = self.__getTweetsLikedUserList(parsed)

        if server is None:
            return response
        else:
            super().return_success_response(response, server)

    def handlePostTweetQuery(self, path, server):
        parsed = super().parse_query_params(path)
        response = {}
        if '/tweet/create' in path:
            response = self.__createTweet(parsed)
        elif '/tweet/delete' in path:
            response = self.__deleteTweet(parsed)
        elif '/tweet/edit' in path:
            response = self.__editTweet(parsed)
        elif 'tweet/like' in path:
            response = self.__likeTweet(parsed)
        elif '/tweet/unlike/' in path:
            response = self.__dislikeTweet(parsed)


        super().return_success_response(response, server)
