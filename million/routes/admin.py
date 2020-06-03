from flask import render_template, jsonify

from ..app import app, db
from ..app.jwt import get

# --- Frontend ---
@app.route('/mastermind')
def panel():
  token = get()
  if not token['admin']:
    return render_template('404.pug', title='404', token=token)
  return render_template('admin/panel.pug', title='Mastermind', token=token)

# --- API ---
@app.route('/api/mastermind/<path>')
def mastermind(db, path='/'):
  token = get()
  if not token['admin']:
    res = jsonify('Unauthorized.')
    res.status_code = 401
    return res

  if path == 'reset':
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

  return jsonify('Not Implemented')

@app.route('/api/genpoc')
def genpoc():
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
