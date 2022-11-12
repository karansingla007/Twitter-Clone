# Creator: Karan Singla
# Date: 6 Nov 2022

import unittest
import json

from api_base.end_point_handler.users_api import UsersApi
from test_api_base.test_api_base import ADMIN_USER_ID, ADMIN_USER_NAME, ADMIN_USER_FULL_NAME, TestApiBase


class TestUserApi(unittest.TestCase, TestApiBase):
    def test_get_all_user_detail(self):
        super().use_mock_database()
        output = UsersApi().handleGetUserQuery('/user/all/details', None)

        self.assertIn(ADMIN_USER_ID, output, 'get all user detail api 1 testcase failed')
        self.assertIn(ADMIN_USER_NAME, output, 'get all user detail api 2 testcase failed')

    def test_get_user_detail(self):
        super().use_mock_database()
        result = json.loads(UsersApi().handleGetUserQuery(f'/user/details?user_id={ADMIN_USER_ID}', None))[0]

        self.assertEqual(result['user_id'], ADMIN_USER_ID, 'get user detail api 1 testcase failed')
        self.assertEqual(result['user_name'], ADMIN_USER_NAME, 'get user detail api 2 testcase failed')
        self.assertEqual(result['name'], ADMIN_USER_FULL_NAME, 'get user detail api 3 testcase failed')

    def test_get_user_follower_list(self):
        super().use_mock_database()
        result = UsersApi().handleGetUserQuery(f'/user/followers?user_id={ADMIN_USER_ID}', None)

        self.assertIn("thegambhirjr7", result, 'get user follower list api 1 testcase failed')
        self.assertIn("kartikryder", result, 'get user follower list api 2 testcase failed')

    def test_get_user_following_list(self):
        super().use_mock_database()
        result = UsersApi().handleGetUserQuery(f'/user/following?user_id={ADMIN_USER_ID}', None)

        self.assertIn("CAPalakSingla2", result, 'get user following list api 1 testcase failed')
        self.assertIn("sdrth", result, 'get user following list api 2 testcase failed')
        self.assertIn("karannagpal96", result, 'get user following list api 3 testcase failed')


if __name__ == '__main__':
    unittest.main()
