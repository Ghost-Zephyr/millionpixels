from flask import render_template, jsonify
from .jwt import get

def index():
  return render_template('index.pug', title='Home', token=get())
def about():
  return render_template('about.pug', title='About', token=get())

def pikk(db, path):
  try:
    n = int(path)
    assert n < 1000
  except:
    res = jsonify('Bad request.')
    res.status_code = 400
    return res
  pikk = []
  for doc in db.poc.find({'y':n}):
    pikk.append({
      'x': doc['x'],
      'y': doc['y'],
      'color': doc['color']
    })
  res = jsonify(pikk)
  res.status_code = 420
  return res

def reset(db):
  token = get()
  if not token['superadmin']:
    res = jsonify('Unauthorized.')
    res.status_code = 401
    return res
  if db.pixels.count_documents({}) > 0:
    db.pixels.delete_many({})
  l = []
  for i in range(0,1000):
    for j in range(0,1000):
      l.append({
        'x': j, 'y': i,
        'color': 'rgb(51, 51, 51)'
      })
  db.pixels.insert_many(l)
  res = jsonify('Updated picture database.')
  res.status_code = 200
  return res

def genpoc(db):
  token = get()
  if not token['superadmin']:
    res = jsonify('Unauthorized.')
    res.status_code = 401
    return res
  if db.poc.count_documents({}) > 0:
    db.poc.delete_many({})
  l = []
  for i in range(0,1000):
    for j in range(0,1000):
      l.append({
        'x': j, 'y': i,
        'color': f'rgb({i/4}, {j/4}, {(i*j)/8})'
      })
  db.poc.insert_many(l)
  res = jsonify('Updated picture database.')
  res.status_code = 200
  return res

def coffee():
  res = jsonify("I'm a teapot")
  res.status_code = 418
  return res
