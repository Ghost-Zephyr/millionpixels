from flask import Flask
from flask_pymongo import PyMongo
import routes.jwt as jwt
import routes

# ----- App Init -----
jwt.keypair = jwt.set_keypair(jwt.read_keyfiles())

app = Flask(__name__)
#app.jinja_env = Environment(loader=FileSystemLoader('pugs'), trim_blocks=True) TODO: to rename templates folder? from jinja2 import Environment, FileSystemLoader
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

'''
from os import getenv
app.debug = bool(getenv('DEBUG', False))
'''

app.config['MONGO_DBNAME'] = 'million'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/million'
db = PyMongo(app).db

# ----- Frontend routes -----
@app.route('/')
def index():
  return routes.index()
@app.route('/about')
def about():
  return routes.about()
@app.route('/login')
def login():
  return routes.user.login()
@app.route('/register')
def registerhtml():
  return routes.user.registerhtml()
@app.route('/profile')
def profile():
  return routes.user.profile()
@app.route('/logout')
def logout():
  return jwt.forntendLogout()

# ----- Admin routes -----
@app.route('/mastermind')
def admin():
  return routes.admin.panel()

@app.route('/api/mastermind/<path>')
def adminapi(path):
  return routes.admin.mastermind(db, path)

@app.route('/api/gen')
def gen():
  return routes.gen(db)

# ----- API -----
@app.route('/pikk/<path>')
def pikk(path):
  return routes.pikk(db, path)
@app.route('/swag')
def swag():
  return routes.swag()

# - user stuff -
@app.route('/api/user/register', methods=['POST'])
def register():
  return routes.user.register(db)
@app.route('/api/user/signin', methods=['POST'])
def signin():
  return jwt.login(db)
@app.route('/api/user/signout')
def signout():
  return jwt.apiLogout()

# --- Easter Egg ---
@app.route("/coffee", methods=['BREW', 'POST'])
def HTCPCPsupport():
  return routes.coffee()

if __name__ == '__main__':
  try:
    from os import getenv
    if getenv('FLASK_ENV') == 'development':
      app.run(host='0.0.0.0', port=8000, debug=True)
  except: pass
  app.run(host='0.0.0.0', port=8000)
