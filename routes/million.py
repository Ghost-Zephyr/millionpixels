from flask import render_template, jsonify
from .jwt import get

def index():
  return render_template('index.pug', title='Home', token=get())

def pikk(db, path): # TODO: fuck around and find best way to split up image loading?
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

'''
  # return whole db
  pikk = {}
  for h in range(0,1000000):
    o = db.poc.find_one({'n':h})
    pikk[o['n']] = {
      'x': o['x'],
      'y': o['y'],
      'color': o['color']
    }
  res = jsonify(pikk)
  res.status_code = 420
  return res

  # retrun generated test result
  o = {}
  h = 0
  for i in range(1,1000):
    for j in range(1,1000):
      o[f'{h}'] = {
        'x': i, 'y': j,
        'color': f'rgb({i/4}, {j/4}, {(i*j)/8})'
      }
      h += 1
  res = jsonify(o)
  res.status_code = 420
  return res



  try:
    n = int(path)
    assert n+1000 <= 1000000
  except:
    res = jsonify('Bad request.')
    res.status_code = 400
    return res
  pikk = {}
  for h in range(n,n+1000):
    o = db.poc.find_one({'y':h})
    pikk[o['y']] = {
      'x': o['x'],
      'y': o['y'],
      'color': o['color']
    }

  h = 0
  for i in range(0,1000):
    for j in range(0,1000):
      l.append({
        'n': h,
        'x': j, 'y': i,
        'color': f'rgb({i/4}, {j/4}, {(i*j)/8})'
      })
      h += 1
'''

def gen(db):
  token = get()
  if not token['admin']:
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

def swag():# TODO: Maybe worth it to try generating svg server side? probly not.
  o = {}
  h = 0
  for i in range(1,1000):
    for j in range(1,1000):
      o[f'{h}'] = {
        'x': i, 'y': j,
        'color': f'rgb({i/4}, {j/4}, {(i*j)/8})'
      }
      h += 1
  res = jsonify(o)
  res.status_code = 420
  return res

def coffee():
  res = jsonify("I'm a teapot")
  res.status_code = 418
  return res
