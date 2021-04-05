# -*- coding: utf-8 -*-
"""query functions for the 5e database"""
from __future__ import annotations
import sys
import requests
from pymongo.errors import ServerSelectionTimeoutError
from pymongo import MongoClient


# TODO typehinting
# TODO fallback to website if mongo is down and vice versa
def query_database(endpoint: str, index=None):
    """query the local database"""
    client: MongoClient = MongoClient()
    try:
        if "dnfo_db" not in client.list_database_names():
            print("Database doesn't exist.")
            print("Build it with `dnfo --build` and try again.")
            sys.exit(1)
    except ServerSelectionTimeoutError as err:
        print("Unable to connect to database. Is `mongod` running?")
        raise SystemExit() from err
    database = client["dnfo_db"]
    try:
        response = database[endpoint].find_one({"index": index}, {"_id": False})
    except NameError:
        response = list(database[endpoint].find({}, {"_id": False}))
    return response


def query_website(endpoint: str, index=None):
    """query the database at dnd5e.co"""
    url: str = f"https://dnd5eapi.co/api/{endpoint}"
    if index:
        url += f"/{index}"
    try:
        response: requests.Response = requests.get(url)
    except requests.exceptions.ConnectionError as err:
        raise SystemExit from err
    if response.status_code != 200:
        print(f"Error: Either {index} is not a valid index or {endpoint} is invalid.")
        sys.exit(1)
    try:
        response_json = response.json()["results"]
    except KeyError:
        response_json = response.json()
    return response_json
