# Creator: Karan Singla
# Date: 12 Oct 2022

# Pure Abstract class ->
from abc import abstractmethod


class DBBase:
    @abstractmethod
    def executeCreateTableQuery(self, query):
        pass

    @abstractmethod
    def executeCreateDatabaseQuery(self):
        pass

    @abstractmethod
    def executeInsertQuery(self, query):
        pass

    @abstractmethod
    def executeQuery(self, query):
        pass

    @abstractmethod
    def executeUseDatabaseQuery(self):
        pass

    @abstractmethod
    def executeSelectQuery(self, query):
        pass
