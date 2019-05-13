#!venv/bin/python

'''
Main flask routes/actions
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

import os, io, json
from datetime import datetime
from socket import gethostname
from flask import \
request,redirect,render_template, url_for, flash, jsonify, g

from glitnir import app
from glitnir.forms import UploadForm 

FILENAME = "uploads/uploaded_file"

#####################
#  Web UI           #
#####################

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	'''
	Homepage 
	'''
	form = UploadForm()

	#POST
	if form.validate_on_submit():
		#filename = secure_filename(form.file.data.filename)
		form.file.data.save(FILENAME) #'uploads/' + filename)
		return redirect(url_for('display'), code=307) #307=preserve method POST
	#GET
	return render_template('index.html', form=form)

#####################
#  Display          #
#####################

#this method can be hit directly or from the "upload flie" form
@app.route("/display", methods=["POST"])
def display():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if request.method == "POST":
		
		if os.path.isfile(FILENAME):
			#this is coming from the UI which saved a file
			inventory_data = #TODO: open file Image.open(FILENAME) #FIXME: we don't need to open the file as image
			#TODO: open file with the right format
			#TODO: process the file's contents and get ready for D3.js

			#TODO: change this entire block to change from image preprocessing to DB reformatting
		if request.files.get("inventory_data"):
			#there is an file in the request, it's an API request
			# read the file
			invetory_data = request.files["inventory_data"].read()
			#image = Image.open(io.BytesIO(image))

		if inventory_data:
			# preprocess the data and prepare it for visualization

			# 
			#data[blah]=blah
			# indicate that the request was a success
			data["success"] = True

			# show some sort of INFO flash message
			flash('SUCCESS. Received responses:\n','message')
			for prediction in data["predictions"]:
				flash( prediction['label']+": "+str(prediction['probability'])+'\n', 'message')

			#if there was an image uploaded, delete it
			if os.path.isfile(FILENAME):
				os.remove(FILENAME)

		else:
			flash('No File received','error')
			logger.error('No file received')

		# return tsome sort of a response? 
		#or he data dictionary as a JSON response
		return jsonify(data)
