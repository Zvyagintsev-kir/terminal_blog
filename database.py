class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    def __init__(self):
        self.uri = ""
        self.database = None

