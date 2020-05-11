from flask import jsonify, redirect
from authlib.jose import jwt
from bcrypt import checkpw

keypair = {}

def set_keypair(keys): # TODO: lots of db stuff and the jwt
  keypair = {
    'private': keys[0],
    'public': keys[1]
  }
  return keypair

def read_keyfiles(folder='jwt-keys'):
  try:
    prvkf = open(f'{folder}/key.pem', 'r')
    pubkf = open(f'{folder}/key.pub', 'r')
    b = prvkf.read(1)
    private_key = b
    while b != '':
        b = prvkf.read(1)
        private_key += b
    b = pubkf.read(1)
    public_key = b
    while b != '':
        b = pubkf.read(1)
        public_key += b
  except:
    print('\033[3mCould not read key files!\033[0m')
    exit()
  finally:
    prvkf.close()
    pubkf.close()
  return private_key, public_key

def login(db):
  try:
    if request.json:
      json = request.json
    else:
      json = request.form
    p = db.user.find_one({ "nick": json['nick'] })
    if checkpw(json['pwd'].encode('utf-8'), p['pwd']):
      token = createToken(db, json['nick'])
      res = jsonify('Token created.')
      res.set_cookie('jwt', token, max_age=60*60*24*7)
      res.status_code = 200
      return res
    else:
      res = jsonify('Wrong password!')
      res.status_code = 401
      return res
  except:
    res = jsonify('Request error.')
    res.status_code = 400
    return res

def createToken(db, nick):
  p = db.user.find_one({ 'nick': nick })
  token = jwt.encode({'alg': 'RS256'}, {
    'nick': p['nick'],
    'admin': p['admin']
  }, keypair['private'])
  return token

def apiLogout():
  res = jsonify('Logged out.')
  res.set_cookie('jwt', '', max_age=0)
  res.status_code = 200
  return res

def forntendLogout():
  res = redirect('/')
  res.set_cookie('jwt', '', max_age=0)
  return res

def get():
  try:
    dec = jwt.decode(request.cookies.get('jwt'), keypair['public'])
    dec.validate()
    return dec
  except:
    return False
