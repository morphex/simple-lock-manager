import os

working_directory_suffix = ".simple-lock-manager"

def get_working_directory():
    return os.environ.get("HOME")

database = get_working_directory() + "/" + working_directory_suffix + "/"
database_lock = database + "_slm.locked"

def get_database():
    return database
