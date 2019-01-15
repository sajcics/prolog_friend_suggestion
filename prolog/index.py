import logging
from spade import pyxf 

# get logger to print logs
#log = logging.getLogger('hello.prolog')
xsb = pyxf.xsb('/home/stella/Flora-2/XSB/bin/xsb')

def getMyFriends():
    # define path to xsb
    
    logging.debug("inside callProlog()")


    xsb.load('osobe.P')
    results = xsb.query('prijatelj(anica, X)')
    logging.error("results: %s", results)
    return results;
