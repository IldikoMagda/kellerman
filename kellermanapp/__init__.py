###This file will pull everything together and tell python this is a package, and initialize it


from flask import Flask
from flask_cache import Cache   #extenstion to handle Cache


app = Flask(__name__)


app.config.from_object('config')  #allows config.py configuration variables to use
app.config.from_pyfile('config.py')  #allows config.py variables to use from INSTANCE folder IF 


cache = Cache(app,config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/')

@cache.cached(timeout=60)  # 60 seconds to keep information in cache, for faster performance

