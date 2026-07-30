# Second version of the assigment, with refinements from your input

from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------------------------------------
# Book Class
# ------------------------------------------------------------
class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }

# ------------------------------------------------------------
# In-Memory "Database"
# ------------------------------------------------------------
books = []

def find_book(book_id):
    for b in books:
        if b.id == book_id:
            return b
    return None

# ------------------------------------------------------------
# API ROUTES
# ------------------------------------------------------------

# GET /books  → return all books
@app.get("/books")
def get_books():
    return jsonify([b.to_dict() for b in books]), 200


# GET /books/<id>  → return one book
@app.get("/books/<int:book_id>")
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.to_dict()), 200


# POST /books  → create a new book
@app.post("/books")
def create_book():
    data = request.json

    # Validate required fields
    required = ["id", "book_name", "author", "publisher"]
    if not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    # Prevent duplicate IDs
    if find_book(data["id"]) is not None:
        return jsonify({"error": "Book with this ID already exists"}), 409

    new_book = Book(
        data["id"],
        data["book_name"],
        data["author"],
        data["publisher"]
    )
    books.append(new_book)

    return jsonify(new_book.to_dict()), 201


# PUT /books/<id>  → update an existing book
@app.put("/books/<int:book_id>")
def update_book(book_id):
    book = find_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    data = request.json

    # Update only provided fields
    if "book_name" in data:
        book.book_name = data["book_name"]
    if "author" in data:
        book.author = data["author"]
    if "publisher" in data:
        book.publisher = data["publisher"]

    return jsonify(book.to_dict()), 200


# DELETE /books/<id>  → delete a book
@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    global books
    book = find_book(book_id)

    if book is None:
        return jsonify({"error": "Book not found"}), 404

    books = [b for b in books if b.id != book_id]
    return jsonify({"message": "Book deleted"}), 200


# ------------------------------------------------------------
# Run the server
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
