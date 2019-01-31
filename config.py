""" Define All essential configurations we will need for the app itself"""
import os

DEBUG = True    # Turns on debugging features in Flask
RELOADER = True
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + 'downloads/'
