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
    if request.method == "POST" or request.method == "PUT":
        if request.method == "POST":
            id = data_store.get_last_id()
        else:
            if request.values.get("book_id"):
                id = int(request.values.get("book_id"))
        title = request.values.get("title")
        author = request.values.get("author")
        country = request.values.get("country")
        book = Book(
            id=id, title=title, author=author, country=country
        )
        if book:
            try:
                data_store.add(book=book)
                return "added"
            except PermissionError:
                return "Excel File is locked"
    if request.method == "DELETE":
        book_id = request.values.get("book_id")
        if book_id:
            return data_store.delete_book(index=int(book_id))
        else:
            return "MIssing inputs"
    return "hi"


app.config["JSON_AS_ASCII"] = False
app.run(host="localhost", port=8000)
