#!venv/bin/python
import logging
import os

class Config (object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
     
    #App run options
    PORT = 5000
    DEBUG_MODE = False
    THREADED_MODE = True
    ENV = 'development' #change to 'production'
    APP_RUN_OPTS = {
        'host':     '0.0.0.0',
        'threaded': THREADED_MODE,
        'port':     PORT,
        'debug':    DEBUG_MODE
    }

    #logging options
    APP_NAME = 'glitnir'
    LOGGING_FORMAT = '%(asctime)-15s %(message)s' #'%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    if DEBUG_MODE:
        LOGGING_LEVEL = logging.DEBUG 
    else:
        LOGGING_LEVEL = logging.INFO
