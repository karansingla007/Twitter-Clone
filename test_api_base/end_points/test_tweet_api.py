import unittest
import json

from api_base.end_point_handler.users_api import UsersApi
from test_api_base.test_api_base import ADMIN_USER_ID, ADMIN_USER_NAME, ADMIN_USER_FULL_NAME, TestApiBase


class TestUserApi(unittest.TestCase, TestApiBase):
    def test_get_all_user_detail(self):
        super().use_mock_database()
        output = UsersApi().getAllUsersDetails()

        self.assertIn(ADMIN_USER_ID, output, 'get all user detail api 1 testcase failed')
        self.assertIn(ADMIN_USER_NAME, output, 'get all user detail api 2 testcase failed')


if __name__ == '__main__':
    unittest.main()
