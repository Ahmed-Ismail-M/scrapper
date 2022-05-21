from flask import Flask
from flask.globals import request

from datastore import DataStore
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        DataStore().add()
        return('hi')
app.run(host='localhost', port=8000)
