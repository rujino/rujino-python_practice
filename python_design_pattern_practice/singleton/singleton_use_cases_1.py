import sqlite3


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)
        print(cls._instance)
        return cls._instance[cls]


class Datebase(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Datebase().connect()
db2 = Datebase().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
