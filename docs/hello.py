#from flask import Flask,abort
from openedoocli.openedoo import *
import json
from datetime import timedelta

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=10)
#db = SQLAlchemy(app)

print "bisa"

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == "__main__":
	app.run()