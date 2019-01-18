import logging
import types
from spade import pyxf 

# load xsb from your computer - have to be installed
# go to Flora-2 download, unzip and ./runflora after that 
# run command 'xsb'. If xsb working then change path 
# in line below
xsb = pyxf.xsb('/home/stella/Flora-2/XSB/bin/xsb')
xsb.load('osobe.P')

# this function gets friends of default user
def getMyFriends(user):
    
    # define path to xsb
    results = xsb.query('all_friends(%s, X)' % user) 

    # results data type DICT ->  {'X': ['name', 'name', 'name']}
    result = parseResultToArray(results)

    logging.error("results for friends: %s", result)
    return result

# this function gets friends of friends which default user is not friend
def getMySuggestions(user):
    results = xsb.query('all_suggestions(%s, X)' % user)

    logging.error("results for suggestions: %s", results)
    # results data type DICT ->  {'X': ['name', 'name', 'name']}
    result = parseResultToArray(results)

    logging.error("results for suggestions: %s", result)
    return result

def parseResultToArray(dictData):
    if type(dictData) == type(True) or type(dictData) == type(False):
        return []

    result = dictData[0]["X"]
    result = result.replace('[', '').replace(']', '')
    result = result.split(',')
    return result