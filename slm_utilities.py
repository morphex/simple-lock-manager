#!/usr/bin/python3

from slm_config import database, lock_suffix
import time
import os
import sys

DEBUG = False

if os.environ.get("DEBUG") == "True":
    DEBUG = True

def DEBUG_PRINT(*arguments):
    if DEBUG:
        print(*arguments, file=sys.stderr)

def get_uptime():
    """Returns the system uptime in seconds as a float."""
    return float(open("/proc/uptime", "r").readline().split()[0])

def generate_lock_filename(lock_name):
    return database + lock_name + lock_suffix    

def write_lock(lock_name):
    """Writes current time into lock_name + lock_suffix"""
    write_lock_filename(generate_lock_filename(lock_name))
    
def write_lock_filename(filename):
    lockfile = open(filename, "x")
    _write_to_lock(lockfile)
    
def _write_to_lock(file):
    file.write(str(time.time()))
    file.flush()    

def delete_lock(lock_name):
    """Removes a given lockfile lock_name + lock_suffix."""
    os.unlink(database + lock_name + lock_suffix)
    
if __name__ == "__main__":
    print("Uptime", get_uptime())
