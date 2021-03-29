"""build the database"""
from pymongo import MongoClient
from dnfo.database_ops.data_vars import DATA_DIR, DB_DIR


def main():
    """:"""
    print(DATA_DIR, DB_DIR)
