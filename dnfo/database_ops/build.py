"""build the database"""
import json
from pymongo import MongoClient
from dnfo import remove_prefix, remove_suffix
from dnfo.database_ops import DB_DIR


def main():
    """:"""
    client: MongoClient = MongoClient()
    database = client["dnfo_db"]
    files = DB_DIR.glob("*.json")
    # TODO check if database exists
    for file in files:
        # standardize the filename to an endpoint name
        col_name: str = remove_prefix(file.name, "5e-SRD-").lower()
        col_name = remove_suffix(file.name, ".json")
        coll = database[col_name]
        with file.open() as json_dat:
            data = json.load(json_dat)
        if isinstance(data, list):
            coll.insert_many(data)
        else:
            coll.insert_one(data)
