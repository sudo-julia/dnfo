# -*- coding: utf-8 -*-
"""important variables for database location"""
from pathlib import Path
import appdirs

NAME: str = "dnfo"
AUTHOR: str = "sudo_julia"
DATA_DIR: str = appdirs.user_data_dir(NAME, AUTHOR)
DB_DIR: Path = Path(f"{DATA_DIR}/dnfo_db")
URL: str = "https://github.com/5e-bits/5e-database"

# TODO option to update database instead of rebuilding
