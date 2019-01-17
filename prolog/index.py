import logging

from spade import pyxf 

# load xsb from your computer - have to be installed
# go to Flora-2 download, unzip and ./runflora after that 
# run command 'xsb'. If xsb working then change path 
# in line below
xsb = pyxf.xsb('/home/stella/Flora-2/XSB/bin/xsb')

# this function gets friends of default user
def getMyFriends(user):
    # define path to xsb
    xsb.load('osobe.P')
    results = xsb.query('all_friends(%s, X)' % user) 

    # results data type DICT ->  {'X': ['name', 'name', 'name']}
    result = results[0]["X"];
    result = result.replace('[', '').replace(']', '')
    result = result.split(',')
    logging.error(type(result))
    logging.error("results for friends: %s", result)
    return result

# this function gets friends of friends which default user is not friend
def getMySuggestions(user):
    xsb.load('osobe.P')
    #results = xsb.query('prijatelj_prijatelja(%s, S)' % user)
    #logging.error("results for suggestions: %s", results)
    return {}