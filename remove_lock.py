#!/usr/bin/python3

import slm_config
import time
import sys
import slm_utilities
from slm_utilities import DEBUG_PRINT
import slm

database = slm_config.get_database()

def print_usage_info():
    print("Syntax Error.  Correct syntax is")
    print()
    print(sys.argv[0], "<lock_name> [retries, default 0], [timeout, default 10.0 seconds]")
    print()
    print("retries is an integer, timeout a float")
    print()
    print("If retries is negative, retry (block) forever")


def remove_lock(lock_name, retries=0, timeout=10.0):
    slm.setup()
    if lock_name == "slm_internal":
        return 255
    try:
        slm_utilities.delete_lock(lock_name)
        return 0
    except Exception as value:
        DEBUG_PRINT("Exception", value)
        if retries > 0 or retries < 0:
            DEBUG_PRINT("Failed to remove lock: ", lock_name, "retrying", retries)
            time.sleep(timeout)
            return remove_lock(lock_name, retries=retries - 1, timeout=timeout)
        return 1

if __name__ == "__main__":
    retries = 0
    timeout = 10.0
    try:
        lock_name = sys.argv[1]
    except IndexError:
        print_usage_info()
        sys.exit(2)
    try:
        retries = sys.argv[2]
        timeout = sys.argv[3]
    except IndexError:
        pass
    try:
        retries = int(retries)
        timeout = float(timeout)
    except ValueError:
        print_usage_info()
        sys.exit(2)
    result = remove_lock(lock_name, retries, timeout)
    if result:
        print("Lock not removed:", lock_name)
    else:
        print("Lock removed:", lock_name)
    sys.exit(result)
