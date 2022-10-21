from sqlite.base.db_impl import DbImpl

dbImpObj = DbImpl()


class SqliteHelper:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

    @staticmethod
    def create_table(query):
        dbImpObj.executeCreateTableQuery(query)

    @staticmethod
    def create_database():
        dbImpObj.executeCreateDatabaseQuery()

    @staticmethod
    def use_database_query():
        dbImpObj.executeUseDatabaseQuery()

    @staticmethod
    def execute_insert_query(query):
        return dbImpObj.executeInsertQuery(query)

    @staticmethod
    def execute_select_query(query):
        print(dbImpObj.executeSelectQuery(query))
        return dbImpObj.executeSelectQuery(query)

    @staticmethod
    def execute_query(query):
        return dbImpObj.executeQuery(query)
