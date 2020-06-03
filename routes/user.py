from flask import request, render_template, redirect, jsonify
from bcrypt import hashpw, gensalt
from .jwt import get, createToken

# ----- Front end user Stuffs -----
def profile():
  token = get()
  if not token:
    return redirect('/')
  return render_template('user/profile.pug', title=f'{token["nick"]}\'s profile', token=token)
def login():
  token = get()
  if token:
    return redirect('/')
  return render_template('user/login.pug', title='Login', token=token)
def registerhtml():
  token = get()
  if token:
    return redirect('/')
  return render_template('user/register.pug', title='Register', token=token)

# ----- register user and JWT -----
def register(db):
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

