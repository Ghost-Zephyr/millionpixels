from flask import request, render_template, redirect, jsonify
from bcrypt import hashpw, gensalt, checkpw

from ..app import app, db
from ..app.jwt import get, createToken

# ----- Frontend routes -----
@app.route('/login')
def login():
  token = get()
  if token:
    return redirect('/')
  return render_template('user/login.pug', title='Login', token=token)

@app.route('/register')
def registerhtml():
  token = get()
  if token:
    return redirect('/')
  return render_template('user/register.pug', title='Register', token=token)

@app.route('/profile')
def profile():
  token = get()
  if not token:
    return redirect('/')
  return render_template('user/profile.pug', title=f'{token["nick"]}\'s profile', token=token)

# --- API routes ---
@app.route('/api/user/register', methods=['POST'])
def register():
  try:
    if request.json:
      json = request.json
    else:
      json = request.form
    if db.user.find_one({ 'nick': json['nick'] }):
      res = jsonify('Nick taken.')
      res.status_code = 409
      return res
    try:
      if json['pwd'] != json['pwd1']:
        res = jsonify('Passwords doesn\'t match!')
        res.status_code = 406
        return res
    except KeyError:
      pass
    db.user.insert_one({
      'nick': json['nick'],
      'pwd': hashpw(json['pwd'].encode('utf-8'), gensalt()),
      'admin': False,
      'superadmin': False,
      'stats': {}
    })
    token = createToken(db, json['nick'])
    res = jsonify('User registered.')
    res.set_cookie('jwt', token, max_age=60*60*24*7)
    res.status_code = 200
    return res
  except:
    res = jsonify('Could not create user.')
    res.status_code = 400
    return res

@app.route('/api/user/signin', methods=['POST'])
def signin():
  try:
    if request.json:
      json = request.json
    else:
      json = request.form
    try:
      p = db.user.find_one({ "nick": json['nick'] })
    except:
      res = jsonify('No such user!')
      res.status_code = 401
      return res
    if not checkpw(json['pwd'].encode('utf-8'), p['pwd']):
      res = jsonify('Wrong password!')
      res.status_code = 401
      return res
    token = createToken(db, json['nick'])
    res = jsonify('Token created.')
    res.set_cookie('jwt', token, max_age=60*60*24*7)
    res.status_code = 200
    return res
  except:
    res = jsonify('Request error.')
    res.status_code = 400
    return res

# --- logout funcs ---
@app.route('/logout')
def logout():
  res = redirect('/')
  res.set_cookie('jwt', '', max_age=0)
  return res

@app.route('/api/user/signout')
def signout():
  res = jsonify('Logged out.')
  res.set_cookie('jwt', '', max_age=0)
  res.status_code = 200
  return res
