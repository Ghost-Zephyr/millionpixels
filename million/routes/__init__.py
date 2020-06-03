from ..app import app, db

from .million import *
from .admin import *
from .user import *

# --- Easter Egg ---
@app.route("/coffee", methods=['BREW', 'POST'])
def HTCPCPsupport():
  res = jsonify("I'm a teapot")
  res.status_code = 418
  return res
