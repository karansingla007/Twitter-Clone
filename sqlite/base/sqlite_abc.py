from abc import abstractmethod


class SqliteAbc:
    # @abstractmethod
    # def executeCreateTableQuery(self, query):
    #     pass

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
