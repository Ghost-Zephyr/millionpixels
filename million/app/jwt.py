from flask import jsonify, redirect, request
from authlib.jose import jwt

keypair = {}

def set_keypair(keys):
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

def createToken(db, nick):
  p = db.user.find_one({ 'nick': nick })
  token = jwt.encode({'alg': 'RS256'}, {
    'nick': p['nick'],
    'admin': p['admin'],
    'superadmin': p['superadmin']
  }, keypair['private'])
  return token

def get():
  try:
    dec = jwt.decode(request.cookies.get('jwt'), keypair['public'])
    dec.validate()
    return dec
  except:
    return None
