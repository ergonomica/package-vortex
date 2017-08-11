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

def vortex(argc):
    """vortex: Navigate around the filesystem.
    
    Usage:
       vortex POINT
       vortex set NAME PATH
       vortex remove NAME...
       vortex list
    """

    env = argc.env
    
    if argc.args['POINT']:
        env.change_directory(VORTEX_MAP[argc.args['POINT']])
     
    elif argc.args['set']:
        VORTEX_MAP.update(kwargs)
        pickle.dump(VORTEX_MAP, open(PATH_TO_MAP, "wb"))
    
    elif argc.args['remove']:
        for vp in argc.args['NAME']:
            del VORTEX_MAP[vp]
            pickle.dump(VORTEX_MAP, open(PATH_TO_MAP, "wb"))

    elif argc.args['list']:
        return [x for x in VORTEX_MAP]
    
exports = {"vortex": vortex}
