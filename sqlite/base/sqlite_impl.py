import pymysql
from sqlite.base.sqlite_abc import SqliteAbc
from sqlite.constants import HOST
from sqlite.constants import USER
from sqlite.constants import PASSWORD


class SqliteImpl(SqliteAbc):

    def __init__(self):
        db = pymysql.connect(host=HOST,
                             user=USER,
                             password=PASSWORD, )
        self.db = db
        self.cursor = db.cursor()
        self.db.autocommit(True)

    def executeCreateDatabaseQuery(self):
        query = '''create database twitterClone'''
        self.cursor.execute(query)

    def executeUseDatabaseQuery(self):
        useDbQuery = '''use twitterClone'''
        self.cursor.execute(useDbQuery)

    def executeCreateTableQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)

    def executeInsertQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def executeSelectQuery(self, query):
        self.cursor.execute(query)
        columns = [d[0] for d in self.cursor.description]
        response = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        print(type(response))
        response = str(response).replace("'", '"')
        return response

    def executeQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
