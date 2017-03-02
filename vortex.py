"""
[vortex.py]

Quick directory aliases.
"""

# for path stuff
import os

# for loading/setting
# vortex map
import pickle

#
# load map if exists
#

# get path to map
PATH_TO_MAP = os.path.join(os.path.expanduser("~"), ".ergo")
PATH_TO_MAP = os.path.join(PATH_TO_MAP, ".pkg-vortex")

try:
    # load map
    VORTEX_MAP = pickle.load(open(PATH_TO_MAP, "rb"))
except IOError: # when the file may not be read
    VORTEX_MAP = {}


def vortex(env, args, kwargs):
    """POINT@Go to vortex point POINT."""
    if len(args) > 1:
        print("[ergo: vortex: ArgumentError]: More than 1 arguments passed.")
    else:
        if args[0] in VORTEX_MAP:
            env.change_directory(VORTEX_MAP[args[0]])

def vortex_set(env, args, kwargs):
    """POINTNAME DIR@Create new vortex point POINTNAME to directory DIR."""

    VORTEX_MAP.update(kwargs)
    pickle.dump(VORTEX_MAP, open(PATH_TO_MAP, "wb"))
    
def vortex_remove(env, args, kwargs):
    """POINT@Delete vortex point POINT."""
    for vp in args:
        del VORTEX_MAP[vp]
    pickle.dump(VORTEX_MAP, open(PATH_TO_MAP, "wb"))

def vortex_list(env, args, kwargs):
    """@List all vortex points."""
    return [i + " -> " + VORTEX_MAP[i] for i in VORTEX_MAP]
    
verbs = {"vortex":vortex,
         "vortex_set":vortex_set,
         "vortex_remove":vortex_remove,
         "vortex_list":vortex_list,
        }
