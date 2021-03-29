"""get and build the database"""
from __future__ import annotations
import json
import shutil
import tempfile
from pathlib import Path
import appdirs
import git


# TODO progress bar!!
# TODO download older release if database breaks
# TODO log git commmit in data_dir
# TODO should i just be downloading the repo lmfao


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
        with open(hash_file, "r") as file:
            oldhash: str = file.read().strip()
        if oldhash != newhash:
            return False
    except FileNotFoundError:
        with open(hash_file) as file:
            file.write(newhash.strip())
    finally:
        return True


def copy_json(source: str, dest: str):
    """move files to data directory"""
    errors: list[str] = []

    print("Copying files to local database...")
    src_dir = Path(source)
    for file in src_dir.glob("*.json"):
        if not validate_json(file):
            errors.append(f"'{file}' does not contain valid JSON data.")
            continue
        shutil.copyfile(file, dest)


def validate_json(file: Path) -> bool:
    """validate a json file, return True if file is valid"""
    try:
        with open(file) as file_loc:
            json.load(file_loc)
    except ValueError:
        return False
    return True


def populate_db():
    """perform the bulk of the operations"""
    appname: str = "dnfo"
    appauthor: str = "sudo_julia"
    data_dir: str = appdirs.user_data_dir(appname, appauthor)  # path to data dir
    db_dir: str = f"{data_dir}/db"  # path to database dir
    hash_file: Path = Path(f"{data_dir}/old_HEAD")
    url: str = "https://github.com/5e-bits/5e-database"

    try:
        print(f"Creating '{db_dir}' for database storage...")
        Path(db_dir).mkdir(parents=True)
    except FileExistsError:
        print(f"'{db_dir}' already exists.")

    with tempfile.TemporaryDirectory(prefix="dnfo.") as tmpdir:
        head_hash = download_db(url, tmpdir)
        if hashes_match(hash_file, head_hash):
            # TODO option to overwrite
            print("Database is already up to date. Cancelling operation.")
            return
        copy_json(tmpdir, db_dir)
