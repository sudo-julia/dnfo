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


def download_db(location: str):
    """make the temporary directory to download files to"""
    print("Cloning database repo...")
    git.Repo.clone_from("https://github.com/5e-bits/5e-database", location)


def copy_files(source: str, dest: str):
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

    try:
        print(f"Creating '{db_dir}' for database storage.")
        Path(db_dir).mkdir(parents=True)
    except FileExistsError:
        print(f"'{db_dir}' already exists.")

    with tempfile.TemporaryDirectory(prefix="dnfo.") as tmpdir:
        download_db(tmpdir)
        copy_files(tmpdir, db_dir)
