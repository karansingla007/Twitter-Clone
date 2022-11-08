from sqlite.sqlite_helper import SqliteHelper

ADMIN_USER_NAME = "karansinglaOO7"
ADMIN_USER_ID = "2811595370"
ADMIN_USER_FULL_NAME = "karan singla"


class TestApiBase:
    def use_mock_database(self):
        SqliteHelper.instance().use_database_query()
