from database_x.database_x import Database_x

class Logic:
    def __init__(self):
        self.database = None
        self.__createDatabase()

    def __createDatabase(self):
        if self.database is None:
            self.database = Database_x()
