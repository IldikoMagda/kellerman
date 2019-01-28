""" Define All essential configurations we will need for the app itself"""
import os


DEBUG = True    # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12  # Configuration for the Flask-Bcrypt extension --see more in whatidid.txt
RELOADER = True
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
