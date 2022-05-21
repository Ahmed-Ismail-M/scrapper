from flask import Flask
from flask.globals import request

from datastore import DataStore
from models.bookModel import Book
from services.ExcelService import ExcelService
app = Flask(__name__)
excel_service = ExcelService(path='test.xlsl')
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        
    if request.method == "POST":
        book = Book(id= int(request.form['id']), title= request.form['title'], auther= request.form['title'])
      ``
        return('hi')
app.run(host='localhost', port=8000)
