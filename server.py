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
        data_store.add(None)
    if request.method == "POST":
        book = Book(
            id=data_store.get_last_id(),
            title=request.values.get("title"),
            author=request.values.get("author"),
        )
        if book:
            data_store.add(book=book)
            return "added"
    return "hi"


app.run(host="localhost", port=8000)
