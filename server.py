from flask import Flask
from flask.globals import request
from datastore import DataStore
from models.bookModel import Book

app = Flask(__name__)
data_store = DataStore()


@app.route("/", methods=["GET", "POST", "DELETE", "PUT"])
def home():
    if request.method == "GET":
        return data_store.get_all_books()
    if request.method == "POST":
        id = data_store.get_last_id()
        title = request.values.get("title")
        author = request.values.get("author")
        country = request.values.get("country")
        try:
            book = Book(id=id, title=title, author=author, country=country)
            if book:
                try:
                    data_store.add(book=book)
                    return f"Added with id: {id}"
                except PermissionError:
                    return "Excel File is locked"
        except ValueError as e:
            return e.__str__()

    if request.method == "PUT":
        id = request.values.get("book_id")
        title = request.values.get("title")
        author = request.values.get("author")
        country = request.values.get("country")
        try:
            book = Book(id=id, title=title, author=author, country=country)
            if book:
                try:
                    data_store.add(book=book)
                    return f"Updated with id: {id}"
                except PermissionError:
                    return "Excel File is locked"
        except ValueError as e:
            return e.__str__()
    if request.method == "DELETE":
        book_id = request.values.get("book_id")
        if book_id:
            return data_store.delete_book(index=int(book_id))
        else:
            return "Missing inputs"


@app.route("/<book_id>", methods=["GET"])
def get_book(book_id):
    if request.method == "GET":
        try:
            if data_store.get_by_id(int(book_id)):
                return data_store.get_by_id(int(book_id))
        except ValueError:
            return "Invalid ID"


app.config["JSON_AS_ASCII"] = False
app.run(host="localhost", port=8000)
