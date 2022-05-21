from flask import Flask
from flask.globals import request

from datastore import DataStore
from models.bookModel import Book
from services.ExcelService import ExcelService

app = Flask(__name__)
data_store = DataStore()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return data_store.get_all_books()
    if request.method == "POST":
        book = Book(
            id=data_store.get_last_id(),
            title=request.values.get("title"),
            author=request.values.get("author"),
            country=request.values.get("country")
        )
        if book:
            try:
                data_store.add(book=book)
            except PermissionError:
                return 'Excel File is locked'
            return "added"
    return "hi"


app.run(host="localhost", port=8000)
