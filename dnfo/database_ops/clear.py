"""clear the local database"""
import shutil
import appdirs


def clear_db() -> int:
    """clear the database to be repopulated"""
    name: str = "dnfo"
    author: str = "sudo_julia"
    data_dir: str = appdirs.user_data_dir(name, author)
    try:
        shutil.rmtree(data_dir)
        print("Successfully cleared database!")
    except PermissionError:
        print(f"Unable to clear database at {data_dir} due to permission errors.")
        return 1
    return 0


if __name__ == "__main__":
    clear_db()
