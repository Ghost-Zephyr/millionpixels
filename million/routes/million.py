from flask import request, render_template, jsonify

from ..app import app, db
from ..app.jwt import get

# --- Frontend ---
@app.route('/')
def index():
  return render_template('index.pug', title='Home', token=get())

@app.route('/about')
def about():
  return render_template('about.pug', title='About', token=get())

@app.route('/pixels')
def pixels():
  return render_template('pixels.pug', title='Edit pixels', token=get())

# --- API ---
@app.route('/pikk/<path>')
def pikk(path):
  try:
    n = int(path)
    assert n < 1000
  except:
    res = jsonify('Bad request.')
    res.status_code = 400
    return res
  pikk = []
  for doc in db.pixels.find({'y':n}):
    pikk.append({
      'x': doc['x'],
      'y': doc['y'],
      'color': doc['color']
    })
  res = jsonify(pikk)
  res.status_code = 420
  return res

@app.route('/api/pixel')
def pixel():
  try:
    if request.json:
      json = request.json
    else:
      json = request.form
    pixel = db.pixels.find_one({ 'x': json['x'], 'y': json['y'] })
    res = jsonify({ 'x': pixel['x'], 'y': pixel['y'], 'color': pixel['color'], 'href': '/' })
    res.status_code = 200
    return res
  except:
    res = jsonify('Bad request.')
    res.status_code = 400
    return res
