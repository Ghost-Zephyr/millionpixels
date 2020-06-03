from million.app import app
from million.routes import *

if __name__ == '__main__':
  try:
    from os import getenv
    if getenv('FLASK_ENV') == 'development':
      app.run(host='0.0.0.0', port=8000, debug=True)
  except: pass
  app.run(host='0.0.0.0', port=8000)
