"""
[vortex.py]


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
path_to_map = os.path.join(os.path.expanduser("~"), ".ergo")
path_to_map = os.path.join(path_to_map, ".pkg-vortex")

try:
    # load map
    _map = pickle.load(open(path_to_map, "rb"))
except IOError: # when the file may not be read
    _map = {}


def vortex(env, args, kwargs):
    """"""
    if len(args) > 1:
        print("[ergo: vortex: ArgumentError]: More than 1 arguments passed.")
    else:
        if args[0] in _map:
            env.change_directory(_map[args[0]])
    
def vortex_set(env, args, kwargs):
    """"""

    _map[args[0]] = args[1]
    pickle.dump(_map, open(path_to_map, "wb"))
        
    
def vortex_remove(env, args, kwargs):
    """"""
    return
    
verbs = {"vortex":vortex,
         "vortex_set":vortex_set,
         "vortex_remove":vortex_remove,
        }
