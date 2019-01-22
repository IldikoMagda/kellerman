<<<<<<< HEAD
import os

from app import app

port = int(os.environ.get('PORT', 33506))
# to run local
#app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port)
# run deployed
app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port, host='0.0.0.0')
=======
""" This File is used to run the app deployed or locally"""
import os
from app import APP

port = int(os.environ.get('PORT', 33506))
# to run local
#APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'])
# run deployed
APP.run(debug=APP.config['DEBUG'], use_reloader=APP.config['RELOADER'], port=port, host='0.0.0.0')
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37
