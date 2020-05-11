from flask import render_template, redirect, jsonify
from .jwt import get

def profile():
  token = get()
  if not token:
    return redirect('/')
  return render_template('user/profile.pug', title=f'{token.nick}\'s profile', token=token)
def login():
  if get():
    return redirect('/')
  return render_template('user/login.pug', title='Login')
def registerhtml():
  if get():
    return redirect('/')
  return render_template('user/register.pug', title='Register')

def register(db):
  try:
    if request.json:
      json = request.json
    else:
      json = request.form
    if db.p.find_one({ 'nick': json['nick'] }):
      res = jsonify("Nick taken.")
      res.status_code = 409
      return res
    try:
      if json['pwd'] != json['pwd1']:
        res = jsonify("Passwords doesn't match!")
        res.status_code = 406
        return res
    except KeyError:
      pass
    db.p.insert_one({
      'nick': json['nick'],
      'pwd': hashpw(json['pwd'].encode('utf-8'), gensalt()),
      'admin': False,
      'stats': {}
    })
    token = createToken(db, json['nick'])
    res = jsonify(token)
    res.set_cookie("jwt", token, max_age=60*60*24*7)
    res.status_code = 200
    return res
  except:
    res = jsonify("Could not create user.")
    res.status_code = 400
    return res

def signin():
  res = jsonify('get fucked')
  res.status_code = 420
  return res

