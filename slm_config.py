import os

working_directory_suffix = ".simple-lock-manager"
lock_suffix = ".lock"

def get_working_directory():
    return os.environ.get("HOME")

database = get_working_directory() + "/" + working_directory_suffix + "/"

def get_database():
    return database
