from flask import render_template, jsonify
from .jwt import get

def index():
  return render_template('index.pug', title='Home', token=get())

def pikk(db):
  pikk = {}
  h = 0
  for h in range(0,1000000):
    o = db.poc.find_one({'n':h})
    pikk[o['n']] = {
      'x': o['x'],
      'y': o['y'],
      'color': o['color']
    }
    h += 1
  res = jsonify(pikk)
  res.status_code = 420
  return res

'''
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
  h = 0
  for i in range(0,1000):
    for j in range(0,1000):
      l.append({
        'n': h,
        'x': i, 'y': j,
        'color': f'rgb({i/4}, {j/4}, {(i*j)/8})'
      })
      h += 1
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
