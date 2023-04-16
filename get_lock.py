#!/usr/bin/python3

import slm_config
import time
import sys
import slm_utilities
from slm_utilities import DEBUG_PRINT
import slm

database = slm_config.get_database()

def get_lock(lock_name):
    slm.setup()
    if lock_name == "slm_internal":
        return 255
    try:
        slm_utilities.write_lock(lock_name)
        return 0
    except Exception as value:
        DEBUG_PRINT("Exception", value)
        return 1

if __name__ == "__main__":
    lock_name = sys.argv[1]
    result = get_lock(lock_name)
    if result:
        print("Lock not acquired:", lock_name)
    else:
        print("Lock acquired:", lock_name)
    sys.exit(result)
