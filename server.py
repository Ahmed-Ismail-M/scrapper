from flask import Flask
from flask.globals import request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return('hi')
app.run(host='localhost', port=8000)
