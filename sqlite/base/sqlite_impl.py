import pymysql
from sqlite.base.sqlite_abc import SqliteAbc


class SqliteImpl(SqliteAbc):

    def __init__(self):
        db = pymysql.connect(host='database-1.ca61zonggiii.ap-south-1.rds.amazonaws.com',
                             user='admin',
                             password='Rinki123*', )
        self.db = db
        self.cursor = db.cursor()
        self.db.autocommit(True)



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
        response =  [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        print(type(response))
        response = str(response).replace("'", '"')
        return response

    def executeQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)

    def executeCreateDatabaseQuery(self):
        query = '''create database twitterClone'''
        self.cursor.execute(query)

    def executeUseDatabaseQuery(self):
        useDbQuery = '''use twitterClone'''
        self.cursor.execute(useDbQuery)

