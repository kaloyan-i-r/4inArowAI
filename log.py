import logging
import inspect

logging.basicConfig(format='%(levelname)s:  %(msg)s',level=logging.DEBUG)

#logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
#logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

def info(msg):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    logging.info(calframe[1][3]+': << '+msg+' >>')

def warn(msg):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    logging.warn(calframe[1][3]+': << '+msg+' >>')