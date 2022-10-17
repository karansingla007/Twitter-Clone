from sqlite.base.sqlite_impl import SqliteImpl

sqlImpObj = SqliteImpl()


class SqliteHelper:
    @staticmethod
    def create_table(self, query):
        sqlImpObj.executeCreateTableQuery(query)

    @staticmethod
    def create_database(self):
        sqlImpObj.executeCreateDatabaseQuery()

    @staticmethod
    def use_database_query(self):
        sqlImpObj.executeUseDatabaseQuery()

    @staticmethod
    def execute_insert_query(self, query):
        return sqlImpObj.executeInsertQuery(query)

    @staticmethod
    def execute_select_query(self, query):
        return sqlImpObj.executeSelectQuery(query)

    @staticmethod
    def execute_query(self, query):
        try:
            sqlImpObj.executeQuery(query)
        except:
            print('error simple execute Query')
