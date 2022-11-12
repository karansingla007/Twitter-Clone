from api_base.api_base import ApiBase
from sqlite.sqlite_helper import SqliteHelper
import json

sqliteHelperObj = SqliteHelper.instance()


class TweetApi(ApiBase):
    def __createTweet(self, parsed):
        """
        Post Api:- Create tweet by user_id
        """
        createTweetQuery = f'''Insert into userTweets(user_id, title, description) values ({parsed['user_id'][0]}, {parsed['title'][0]}, {parsed['description'][0]})'''
        sqliteHelperObj.execute_insert_query(createTweetQuery)

        __response__ = {'response': 200, 'status': 'created'}
        return __response__

    def __deleteTweet(self, parsed):
        """
        Post Api:- delete tweet by tweet_id
        """
        createTweetQuery = f'''Delete from userTweets where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        __response__ = {'response': 200, 'status': 'deleted'}
        return __response__


    def __editTweet(self, parsed):
        """
        Post Api:- edit tweet by tweet_id
        """
        createTweetQuery = f'''Update userTweets set title = {parsed['title'][0]}, description = {parsed['description'][0]} where user_id = {parsed['user_id'][0]} And tweet_id = {parsed['tweet_id'][0]}'''
        sqliteHelperObj.execute_query(createTweetQuery)

        __response__ = {'response': 200, 'status': 'edited'}
        return __response__

    def __likeTweet(self, parsed):
        """
        Post Api:- like tweet by tweet_id
        """
        checkLikeQuery = f'''select status from userLikes where user_id = {parsed['user_id'][0]}  and tweet_id = {parsed['tweet_id'][0]}'''
        checkLike = sqliteHelperObj.execute_select_query(checkLikeQuery)
        json_object = json.loads(checkLike)
        if len(json_object) > 0 and json_object[0]['status'] == 0:
            __response__ = {'response': 400, 'status': 'Already liked tweet'}
        else:
            createLikeQuery = f'''Insert into userLikes(user_id, tweet_id, status) values ({parsed['user_id'][0]}, {parsed['tweet_id'][0]}, 0)'''
            sqliteHelperObj.execute_insert_query(createLikeQuery)
            __response__ = {'response': 200, 'status': 'Liked tweet'}
        return __response__

    def __unLikeTweet(self, parsed):
        """
        Post Api:- unlike tweet by tweet_id
        """
        checkDislikeQuery = f'''select status from userLikes where user_id = {parsed['user_id'][0]} and tweet_id = {parsed['tweet_id'][0]}'''
        checkDislike = sqliteHelperObj.execute_select_query(checkDislikeQuery)
        json_object = json.loads(checkDislike)
        if len(json_object) > 0 and json_object[0]['status'] == 1:
            __response__ = {'response': 400, 'status': 'user has no like'}
        else:
            createDislikeQuery = f'''Insert into userLikes(user_id, tweet_id, status) values ({parsed['user_id'][0]}, {parsed['tweet_id'][0]}, 1)'''
            sqliteHelperObj.execute_insert_query(createDislikeQuery)
            __response__ = {'response': 200, 'status': 'Disliked tweet'}
        return __response__

    def __getTweetsFromUser(self, parsed):
        """
        Get Api:- get tweet of user by user_name
        """
        selectUserTweetsQuery = f'''Select userTweets.tweet_id, userTweets.title, userTweets.description from user Inner Join userTweets on user.user_id = userTweets.user_id where user.user_name = {parsed['user_name'][0]}'''

        __response__ = sqliteHelperObj.execute_select_query(selectUserTweetsQuery)
        return __response__

    def __getTweetsLikedUserList(self, parsed):
        """
        Get Api:- get user list who liked tweet
        """
        selectLikedTweetsQuery = f'''Select user.user_id, user.user_name, user.name, user.bio from user Inner Join userLikes on user.user_id = userLikes.user_id where userLikes.tweet_id = {parsed['tweet_id'][0]} And userLikes.status = 0'''
        __response__ = sqliteHelperObj.execute_select_query(selectLikedTweetsQuery)
        return __response__

    def handleGetTweetQuery(self, path, server):
        """
        Handle rotes of tweet get api
        """
        parsed = super().parse_query_params(path)
        __response__ = {}

        if '/tweet/list/by/userName' in path:
            __response__ = self.__getTweetsFromUser(parsed)
        elif 'tweet/like/list' in path:
            __response__ = self.__getTweetsLikedUserList(parsed)

        if server is None:
            return __response__
        else:
            super().return_success_response(__response__, server)

    def handlePostTweetQuery(self, path, server):
        """
        Handle rotes of tweet post api
        """
        parsed = super().parse_query_params(path)
        __response__ = {}
        if '/tweet/create' in path:
            __response__ = self.__createTweet(parsed)
        elif '/tweet/delete' in path:
            __response__ = self.__deleteTweet(parsed)
        elif '/tweet/edit' in path:
            __response__ = self.__editTweet(parsed)
        elif 'tweet/like' in path:
            __response__ = self.__likeTweet(parsed)
        elif '/tweet/unlike/' in path:
            __response__ = self.__unLikeTweet(parsed)

        super().return_success_response(__response__, server)
