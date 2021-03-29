"""clear the local database"""
import shutil
from dnfo.database_ops.data_vars import DATA_DIR


def clear_db() -> int:
    """clear the database to be repopulated"""
    try:
        shutil.rmtree(DATA_DIR)
        print("Successfully cleared database!")
    except PermissionError:
        print(f"Unable to clear database at {DATA_DIR} due to permission errors.")
        return 1
    return 0


if __name__ == "__main__":
    clear_db()
