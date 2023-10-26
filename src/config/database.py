from pymongo import MongoClient
from src.config.var_env import var_env
class Database():
    def __init__(self):
        self.client = MongoClient(var_env.db_connection)
        self.main = self.client[var_env.database]

database = Database()
