from flask import render_template
from run import app


@app.route("/")
def index():
    return render_template('/index.html')


@app.route("/hello")
def hello():
    app.logger.debug('=debug測試=')
    app.logger.warning('=警告測試 (%d)=', 42)
    app.logger.error('=error測試=')
    return "Hello World!"
