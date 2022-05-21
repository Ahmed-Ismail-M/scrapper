from flask import Flask
from flask.globals import request

from datastore import DataStore
from models.bookModel import Book
from services.ExcelService import ExcelService

app = Flask(__name__)
data_store = DataStore()


@app.route("/", methods=["GET", "POST", "DELETE", "PUT"])
def home():
    if request.method == "GET":
        return data_store.get_all_books()
    if request.method == "POST":
        id=data_store.get_last_id()
        title=request.values.get("title")
        author=request.values.get("author")
        country=request.values.get("country")
        if id and title and author and country:
            book = Book(
                id=data_store.get_last_id(),
                title=title,
                author=author,
                country=country
        )
            if book:
                try:
                    data_store.add(book=book)
                    return "added"
                except PermissionError:
                    return 'Excel File is locked'
        else:
            return 'Missing inputs'
           
    if request.method == "DELETE":
        book_id = request.values.get('book_id')

    return "hi"

app.config['JSON_AS_ASCII'] = False
app.run(host="localhost", port=8000)
