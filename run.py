#!venv/bin/python

# Start the server:
# 	python run.py
# Start the server with docker:
#   docker run -p 5000:5000 fernandosanchez/glitnir
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'

import logging, sys

import glitnir
from config import Config

#init logger
logging.basicConfig(format=Config.LOGGING_FORMAT)
logger = logging.getLogger(Config.APP_NAME)
logger.setLevel(Config.LOGGING_LEVEL)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(Config.LOGGING_LEVEL)
formatter = logging.Formatter(Config.LOGGING_FORMAT)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('logging initialized')

# if this is the main thread of execution 
# initialize app and logging infrastructure. Then
# first load the model and
# then start the server
if __name__ == '__main__':
    logger.debug('About to run')
    #initialize WSGI logger if this is the main thread
    gunicorn_logger=logging.getLogger('gunicorn.error')
    glitnir.app.logger.handlers = gunicorn_logger.handlers
    glitnir.app.logger.setLevel(gunicorn_logger.level)
    #Initialization code
    logger.info('Starting Flask server...')
    logger.info('Please wait until server has fully started')
    #run App
    logger.debug( "Running with options: {}".format(Config.APP_RUN_OPTS) )
    glitnir.app.run(**Config.APP_RUN_OPTS)
    #Tensorflow has trouble unless options are:
    #app.run(debug = False, threaded = False, host='0.0.0.0', port=5000)

