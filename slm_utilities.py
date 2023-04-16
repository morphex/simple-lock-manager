#!/usr/bin/python3

from slm_config import database, lock_suffix
import time
import os
import sys

DEBUG = False

def DEBUG_PRINT(*arguments):
    if DEBUG:
        print(*arguments, file=sys.stderr)

def get_uptime():
    """Returns the system uptime in seconds as a float."""
    return float(open("/proc/uptime", "r").readline().split()[0])

def write_lock(lock_name):
    """Writes current time into lock_name + lock_suffix"""
    lock = open(database + lock_name + lock_suffix, "x")
    lock.write(str(time.time()))
    lock.flush()

def delete_lock(lock_name):
    """Removes a given lockfile lock_name + lock_suffix."""
    os.unlink(database + lock_name + lock_suffix)
    
if __name__ == "__main__":
    print("Uptime", get_uptime())
