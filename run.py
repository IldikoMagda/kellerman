""" This File is used to run the app deployed or locally"""
import os
from app import APP

port = int(os.environ.get('PORT', 33506))
# to run local
#APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'])
# run deployed
APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'], port=port, host='0.0.0.0')
