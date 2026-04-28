from mongita import MongitaClientDisk
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
client = MongitaClientDisk(os.path.join(BASE_DIR, "mongita_data"))

db = client.bookstore
categories_col = db.categories
books_col = db.books

categories_col.delete_many({})
books_col.delete_many({})

categories = [
    {"id": 1, "name": "Fiction"},
    {"id": 2, "name": "Science"},
    {"id": 3, "name": "History"},
    {"id": 4, "name": "Technology"}
]

books = [
    {
        "id": 1,
        "categoryId": 1,
        "categoryName": "Fiction",
        "title": "The Women",
        "author": "Kristin Hannah",
        "isbn": "1250178630",
        "price": 20.58,
        "image": "women.jpg",
        "readNow": 1
    },
    {
        "id": 2,
        "categoryId": 1,
        "categoryName": "Fiction",
        "title": "The Covenant of Water",
        "author": "Abraham Verghese",
        "isbn": "0802162177",
        "price": 19.25,
        "image": "water.jpg",
        "readNow": 0
    },
    {
        "id": 3,
        "categoryId": 1,
        "categoryName": "Fiction",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "0060935464",
        "price": 8.74,
        "image": "mockingbird.jpg",
        "readNow": 1
    },
    {
        "id": 4,
        "categoryId": 2,
        "categoryName": "Science",
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "isbn": "9780553380163",
        "price": 12.99,
        "image": "time.jpg",
        "readNow": 1
    },
    {
        "id": 5,
        "categoryId": 2,
        "categoryName": "Science",
        "title": "The Selfish Gene",
        "author": "Richard Dawkins",
        "isbn": "0199291152",
        "price": 18.20,
        "image": "gene.jpg",
        "readNow": 0
    },
    {
        "id": 6,
        "categoryId": 2,
        "categoryName": "Science",
        "title": "Cosmos",
        "author": "Carl Sagan",
        "isbn": "9780345539434",
        "price": 15.10,
        "image": "cosmos.jpg",
        "readNow": 1
    },
    {
        "id": 7,
        "categoryId": 3,
        "categoryName": "History",
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "isbn": "0062316095",
        "price": 21.96,
        "image": "sapiens.jpg",
        "readNow": 1
    },
    {
        "id": 8,
        "categoryId": 3,
        "categoryName": "History",
        "title": "Guns, Germs, and Steel",
        "author": "Jared Diamond",
        "isbn": "0393317552",
        "price": 18.99,
        "image": "guns.jpg",
        "readNow": 0
    },
    {
        "id": 9,
        "categoryId": 3,
        "categoryName": "History",
        "title": "The Silk Roads",
        "author": "Peter Frankopan",
        "isbn": "1101912375",
        "price": 12.99,
        "image": "silk.jpg",
        "readNow": 1
    },
    {
        "id": 10,
        "categoryId": 4,
        "categoryName": "Technology",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "price": 26.26,
        "image": "clean.jpg",
        "readNow": 1
    },
    {
        "id": 11,
        "categoryId": 4,
        "categoryName": "Technology",
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "isbn": "9780201616224",
        "price": 65.07,
        "image": "pragmatic.jpg",
        "readNow": 1
    },
    {
        "id": 12,
        "categoryId": 4,
        "categoryName": "Technology",
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "isbn": "9780262033848",
        "price": 89.99,
        "image": "algo.jpg",
        "readNow": 0
    }
]

categories_col.insert_many(categories)
books_col.insert_many(books)

with open("categories.json", "w") as f:
    json.dump(categories, f, indent=2)

with open("books.json", "w") as f:
    json.dump(books, f, indent=2)

print("Database seeded successfully.")
print("categories.json and books.json exported.")
