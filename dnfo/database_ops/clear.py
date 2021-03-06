# -*- coding: utf-8 -*-
"""clear the local database"""
import shutil
from pymongo import MongoClient
from dnfo.database_ops import DATA_DIR


def clear_db() -> int:
    """clear the database to be repopulated"""
    try:
        shutil.rmtree(DATA_DIR)
        MongoClient().drop_database("dnfo_db")
        print("Successfully cleared database!")
    except PermissionError:
        print(f"Unable to clear database at {DATA_DIR} due to permission errors.")
        return 1
    return 0


if __name__ == "__main__":
    clear_db()
