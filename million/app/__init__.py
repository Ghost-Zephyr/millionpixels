from flask import Flask
from flask_pymongo import PyMongo

from . import jwt

# ----- App Init -----
jwt.keypair = jwt.set_keypair(jwt.read_keyfiles())

app = Flask(__name__)
#app.jinja_env = Environment(loader=FileSystemLoader('pugs'), trim_blocks=True) # TODO: to rename templates folder? from jinja2 import Environment, FileSystemLoader
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

app.config['MONGO_DBNAME'] = 'million'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/million'
db = PyMongo(app).db
