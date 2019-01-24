<<<<<<< HEAD
import os

from app import app

port = int(os.environ.get('PORT', 33506))
# to run local
app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port)
# run deployed
#app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port, host='0.0.0.0')
=======
import os

from app import app

port = int(os.environ.get('PORT', 33506))
# to run local
#app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port)
# run deployed
app.run(debug=app.config['DEBUG'], use_reloader=app.config['RELOADER'], port=port, host='0.0.0.0')
>>>>>>> 10b9717a694bb439ed9c3fe20f828671c6d57e3e
