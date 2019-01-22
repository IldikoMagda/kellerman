""" This File is used to run the app deployed or locally"""
import os
from app import APP

PORT = int(os.environ.get('PORT', 33506))
# to run local
#APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'])
# run deployed
APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'], PORT=PORT, host='0.0.0.0')
