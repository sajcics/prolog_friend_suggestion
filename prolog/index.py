import types
from spade import pyxf 

# load xsb from your computer - have to be installed
# go to Flora-2 download, unzip and ./runflora after that 
# run command 'xsb'. If xsb working then change path 
# in line below
xsb = pyxf.xsb('/home/stella/Flora-2/XSB/bin/xsb')
xsb.load('osobe.P')

def getMyFriends(user):
    # define path to xsb
    results = xsb.query('all_friends(%s, X)' % user) 

    return parseResultToArray(results)

def getMySuggestions(user):
    results = xsb.query('all_suggestions(%s, X)' % user)
    return parseResultToArray(results)

def addNewFriend(user, friend):
    query = "asserta(friends('%s', '%s'))." % (user, friend)
    xsb.query(query)


def parseResultToArray(dictData):
    if type(dictData) == type(True) or type(dictData) == type(False):
        return []

    result = dictData[0]["X"]
    result = result.replace('[', '').replace(']', '')
    result = result.split(',')
    return result