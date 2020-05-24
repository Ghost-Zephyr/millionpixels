from flask import request, render_template, redirect, jsonify
from .jwt import get, createToken

def r404():
  res = jsonify('Not Found')
  res.status_code = 404
  return res

def panel():
  token = get()
  if not token['admin']:
    return r404()
  return render_template('admin/panel.pug', title='Mastermind', token=token)

def mastermind(db, path='/'):
  token = get()
  if not token['admin']:
    return r404()
  return jsonify('Not Implemented')

