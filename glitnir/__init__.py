#!venv/bin/python
import logging, sys, os, datetime

from flask import Flask, g

from config import Config

#create app
#init handlers and flask app
app = Flask(__name__)
app.config.from_object(Config)
app.env = Config.ENV

from glitnir import views, model

#model.load_model()

