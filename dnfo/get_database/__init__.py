"""get and build the database"""
from __future__ import annotations
import json
import shutil
import tempfile
from pathlib import Path
from typing import Generator
import appdirs
import git


# TODO progress bar!!
# TODO download older release if database breaks


def download_db(url: str, location: str) -> str:
    """clone a repo and return the hash of HEAD"""
    print("Cloning database repo...")
    repo: git.Repo = git.Repo.clone_from(url, location)
    hexsha: str = repo.head.object.hexsha
    return hexsha


def hashes_match(hash_file: Path, newhash: str, force=None) -> bool:
    """compare the hash of recently pulled repo with the stored hash
    returns True if hashes match. returns False if the hashes are different.
    """
    try:
        with open(hash_file, "r") as file:
            oldhash: str = file.read().strip()
        if oldhash == newhash and not force:
            return False
    except FileNotFoundError:
        pass
    finally:
        with open(hash_file, "w") as file:
            file.write(newhash.strip())
        return True  # pylint: disable=W0150


def copy_json(source: str, dest: str) -> bool:
    """move files to data directory"""
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
    """validate a json file, return True if file is valid"""
    try:
        with open(file) as file_loc:
            json.load(file_loc)
    except ValueError:
        return False
    return True


def populate_db(name: str, author: str) -> int:
    """perform the bulk of the operations"""
    data_dir: str = appdirs.user_data_dir(name, author)  # path to data dir
    db_dir: str = f"{data_dir}/db"  # path to database dir
    hash_file: Path = Path(f"{data_dir}/old_HEAD")
    url: str = "https://github.com/5e-bits/5e-database"  # url for database

    try:
        print(f"Creating '{db_dir}' for database storage...")
        Path(db_dir).mkdir(parents=True)
    except FileExistsError:
        print("Using existing database.")

    with tempfile.TemporaryDirectory(prefix="dnfo.") as tmpdir:
        head_hash = download_db(url, tmpdir)
        if hashes_match(hash_file, head_hash):
            # TODO option to overwrite
            print("Database is already up to date. Cancelling operation.")
            return 0
        if not copy_json(tmpdir, db_dir):
            print("Error copying JSON.")
            return 1
    return 0


def clear_db():
    """clear the database to be repopulated"""
    ...


if __name__ == "__main__":
    populate_db("dnfo", "sudo_julia")
