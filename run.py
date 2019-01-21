import os

from app import app

port = int(os.environ.get('PORT', 33506))
# to run local
app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port)
# run deployed
#app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port, host='0.0.0.0')