"""build the database"""
from __future__ import annotations
import json
import shutil
import tempfile
from pathlib import Path
from typing import Generator
import git
from pymongo import MongoClient
from dnfo import remove_prefix, remove_suffix
from dnfo.database_ops import DATA_DIR, DB_DIR, URL


# TODO download older release if database breaks
# TODO put these in a class with clear as a method


def download_db(url: str, location: str) -> str:
    """clone a repo and return the hash of HEAD"""
    print("Cloning database repo...")
    repo: git.Repo = git.Repo.clone_from(url, location)
    hexsha: str = repo.head.object.hexsha
    return hexsha


def hashes_match(hash_file: Path, newhash: str) -> bool:
    """compare the hash of recently pulled repo with the stored hash
    returns True if hashes match. returns False if the hashes are different.
    """
    try:
        with hash_file.open() as file:
            oldhash: str = file.read().strip()
        if oldhash == newhash:
            return False
    except FileNotFoundError:
        pass
    finally:
        with hash_file.open() as file:
            file.write(newhash.strip())
        return True  # pylint: disable=W0150


def dir_empty(dir_path: Path) -> bool:
    """check if a directory is empty
    return True if empty
    """
    has_next = next(dir_path.iterdir(), None)
    if not has_next:
        return True
    return False


def copy_json(source: str, dest: Path) -> bool:
    """move all json files from source to dest
    return True if successful
    """
    print("Copying files to local database...")
    src_dir = Path(f"{source}/src")
    json_files: Generator = src_dir.glob("*.json")

    for file in json_files:
        # TODO display errors properly
        if not validate_json(file):
            print(f"'{file}' does not contain valid JSON data.\nAborting operation.")
            return False
        shutil.copyfile(file, f"{dest}/{file.name}")
    return True


def validate_json(file: Path) -> bool:
    """validate a json file
    return True if file is valid
    """
    try:
        with file.open() as file_loc:
            json.load(file_loc)
    except ValueError:
        return False
    return True


def populate_db() -> int:
    """perform the bulk of the operations"""
    hash_file: Path = Path(f"{DATA_DIR}/old_HEAD")

    try:
        print(f"Creating '{DB_DIR}' for database storage...")
        DB_DIR.mkdir(parents=True)
    except FileExistsError:
        print("Using existing database.")

    with tempfile.TemporaryDirectory(prefix="dnfo.") as tmpdir:
        head_hash = download_db(URL, tmpdir)
        if hashes_match(hash_file, head_hash) and not dir_empty(DB_DIR):
            print("Database is already up to date. Cancelling operation.")
            return 0
        if not copy_json(tmpdir, DB_DIR):
            print("Error copying JSON.")
            return 1
    build()
    print("Database populated successfully!")
    return 0


def build(rebuild=None):
    """insert all documents into the database"""
    client: MongoClient = MongoClient()
    # TODO rebuild option
    if "dnfo_db" in client.list_database_names() and not rebuild:
        print("Database already exists!")
        return
    database = client["dnfo_db"]
    files = DB_DIR.glob("*.json")
    for file in files:
        # standardize the filename to an endpoint name
        col_name: str = remove_prefix(file.name, "5e-SRD-")
        col_name = remove_suffix(col_name, ".json").lower()
        coll = database[col_name]
        with file.open() as json_dat:
            data = json.load(json_dat)
        if isinstance(data, list):
            coll.insert_many(data)
        else:
            coll.insert_one(data)
    print("All documents successfully inserted into the database!")


def lock():
    """create a lockfile containing a hash and the last checked date"""
    # TODO option to suggest the user to rebuild the database every week,
    #      with the last date read from the lockfile
    ...
