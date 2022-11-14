  # Date: 20 Oct 2022

from sqlite.base.db_impl import DbImpl


class SqliteHelper:
    __dbImpObj = DbImpl()
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

    def create_table(self, query):
        self.__dbImpObj.executeCreateTableQuery(query)

    def create_database(self):
        self.__dbImpObj.executeCreateDatabaseQuery()

    def use_database_query(self):
        self.__dbImpObj.executeUseDatabaseQuery()

    def execute_insert_query(self, query):
        return self.__dbImpObj.executeInsertQuery(query)

    def execute_select_query(self, query):
        return self.__dbImpObj.executeSelectQuery(query)

    def execute_query(self, query):
        return self.__dbImpObj.executeQuery(query)
