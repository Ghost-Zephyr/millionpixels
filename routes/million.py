from flask import render_template, jsonify
from .jwt import get

def index():
  return render_template('index.pug', title='Home', token=get())

def pikk():
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
