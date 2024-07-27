class Database:
    def __init__(self):
        self.data = {}

    def save(self, user_id, state):
        self.data[user_id] = state

    def load(self, user_id):
        return self.data.get(user_id, {})

database = Database()
