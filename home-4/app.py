from flask import Flask, render_template, request, redirect, url_for
from mongita import MongitaClientDisk
import os
import json

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
client = MongitaClientDisk(os.path.join(BASE_DIR, "mongita_data"))

db = client.bookstore
categories_col = db.categories
books_col = db.books


def get_categories():
    categories = list(categories_col.find())
    return sorted(categories, key=lambda c: c["id"])


def get_books():
    books = list(books_col.find())
    return sorted(books, key=lambda b: b["id"])


def get_next_book_id():
    books = list(books_col.find())

    if len(books) == 0:
        return 1

    return max(book["id"] for book in books) + 1


def export_json():
    categories = list(categories_col.find())
    books = list(books_col.find())

    for category in categories:
        category.pop("_id", None)

    for book in books:
        book.pop("_id", None)

    with open("categories.json", "w") as f:
        json.dump(categories, f, indent=2)

    with open("books.json", "w") as f:
        json.dump(books, f, indent=2)


@app.route("/")
def index():
    categories = get_categories()
    return render_template("index.html", categories=categories)


@app.route("/read")
def read():
    books = get_books()
    categories = get_categories()
    return render_template("read.html", books=books, categories=categories)


@app.route("/create")
def create():
    categories = get_categories()
    return render_template("create.html", categories=categories)


@app.route("/create_post", methods=["POST"])
def create_post():
    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("isbn")
    price = float(request.form.get("price"))
    category_id = int(request.form.get("categoryId"))
    image = request.form.get("image")
    read_now = int(request.form.get("readNow"))

    category = categories_col.find_one({"id": category_id})

    new_book = {
        "id": get_next_book_id(),
        "categoryId": category_id,
        "categoryName": category["name"],
        "title": title,
        "author": author,
        "isbn": isbn,
        "price": price,
        "image": image,
        "readNow": read_now
    }

    books_col.insert_one(new_book)
    export_json()

    return redirect(url_for("read"))


@app.route("/edit/<int:id>")
def edit(id):
    book = books_col.find_one({"id": id})
    categories = get_categories()

    if book is None:
        return render_template("error.html", message="Book not found.")

    return render_template("edit.html", book=book, categories=categories)


@app.route("/edit_post/<int:id>", methods=["POST"])
def edit_post(id):
    title = request.form.get("title")
    author = request.form.get("author")
    isbn = request.form.get("isbn")
    price = float(request.form.get("price"))
    category_id = int(request.form.get("categoryId"))
    image = request.form.get("image")
    read_now = int(request.form.get("readNow"))

    category = categories_col.find_one({"id": category_id})

    updated_book = {
        "id": id,
        "categoryId": category_id,
        "categoryName": category["name"],
        "title": title,
        "author": author,
        "isbn": isbn,
        "price": price,
        "image": image,
        "readNow": read_now
    }

    books_col.replace_one({"id": id}, updated_book)
    export_json()

    return redirect(url_for("read"))


@app.route("/delete/<int:id>")
def delete(id):
    books_col.delete_one({"id": id})
    export_json()

    return redirect(url_for("read"))


if __name__ == "__main__":
    export_json()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
