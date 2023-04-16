#!/usr/bin/python3

import sys, os, slm_config, slm_utilities, pathlib, time
from slm_utilities import DEBUG_PRINT

#print(os.path.realpath(__file__))

database = slm_config.get_database()
database_lock_file = database + "slm_internal" + ".lock"
database_lock_file = pathlib.Path(database_lock_file)

def setup():
    if not os.path.isdir(database):
        os.mkdir(database)
        slm_utilities.write_lock("slm_internal")
    elif not database_lock_file.exists():
        slm_utilities.write_lock("slm_internal")
    else:
        uptime = slm_utilities.get_uptime()
        modified = database_lock_file.stat().st_mtime
        current_time = time.time()
        if modified > (current_time - uptime):
            DEBUG_PRINT("Fresh internal lock file")
            DEBUG_PRINT(modified, uptime, time.time())
        else:
            DEBUG_PRINT("Stale internal lock file")
            slm_utilities.delete_lock("slm_internal")
            slm_utilities.write_lock("slm_internal")
