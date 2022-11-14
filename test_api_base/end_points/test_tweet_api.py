  # Date: 6 Nov 2022


import unittest

from api_base.end_point_handler.tweet_api import TweetApi
from test_api_base.test_api_base import ADMIN_USER_NAME, TestApiBase


class TestTweetApi(unittest.TestCase, TestApiBase):
    def test_get_tweets_from_user(self):
        super().use_mock_database()
        output = TweetApi().handleGetTweetQuery(f'/tweet/list/by/userName?user_name="{ADMIN_USER_NAME}"', None)

        self.assertIn('''"tweet_id": 4''', output, 'get tweet from user api 1 testcase failed')

    def test_get_tweets_liked_user_list(self):
        super().use_mock_database()
        output = TweetApi().handleGetTweetQuery(f'tweet/like/list?tweet_id=5', None)

        self.assertIn("2811595370", output, 'get tweet from user api 1 testcase failed')
        self.assertIn("606066960", output, 'get tweet from user api 2 testcase failed')


if __name__ == '__main__':
    unittest.main()
