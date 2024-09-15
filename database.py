class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, user):
        self.data[username] = user

    def __getitem__(self, item):
        return self.data[item]
