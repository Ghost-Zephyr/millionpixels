from flask import Flask
import routes

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

from flask import render_template
@app.route('/')
def index():
  return render_template('index.pug', title='home')
#app.add_url_rule('/', 'index', routes.index())

if __name__ == '__main__':
  app.run()
