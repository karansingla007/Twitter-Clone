from sqlite.base.sqlite_impl import SqliteImpl

sqlImpObj = SqliteImpl()

class SqliteHelper:
    def createTable(self, query):
        sqlImpObj.executeCreateTableQuery(query)


    def createDatabase(self):
        sqlImpObj.executeCreateDatabaseQuery()

    def useDatabaseQuery(self):
        sqlImpObj.executeUseDatabaseQuery()

    def executeInsertQuery(self, query):
        return sqlImpObj.executeInsertQuery(query)

    def executeSelectQuery(self, query):
        return sqlImpObj.executeSelectQuery(query)

    def executeQuery(self, query):
        try:
            sqlImpObj.executeQuery(query)
        except:
            print('error simple execute Query')
