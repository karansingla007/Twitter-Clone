import unittest

from api_base.end_point_handler.feed_api import FeedApi
from test_api_base.test_api_base import ADMIN_USER_NAME, TestApiBase


class TestFeedApi(unittest.TestCase, TestApiBase):
    def test_get_tweets_from_user(self):
        super().use_mock_database()
        output = FeedApi().handleGetFeedQuery(f'/feed/by/userName?user_name="{ADMIN_USER_NAME}"', None)

        self.assertIn("tweet_id", output, 'get tweet from user api 1 testcase failed')
        self.assertIn("description", output, 'get tweet from user api 2 testcase failed')


if __name__ == '__main__':
    unittest.main()
