from sqlite.base.sqlite_impl import SqliteImpl

sqlImpObj = SqliteImpl()


class SqliteHelper:
    @staticmethod
    def create_table(query):
        sqlImpObj.executeCreateTableQuery(query)

    @staticmethod
    def create_database():
        sqlImpObj.executeCreateDatabaseQuery()

    @staticmethod
    def use_database_query():
        sqlImpObj.executeUseDatabaseQuery()

    @staticmethod
    def execute_insert_query(query):
        return sqlImpObj.executeInsertQuery(query)

    @staticmethod
    def execute_select_query(query):
        return sqlImpObj.executeSelectQuery(query)

    @staticmethod
    def execute_query(query):
        try:
            sqlImpObj.executeQuery(query)
        except:
            print('error simple execute Query')
