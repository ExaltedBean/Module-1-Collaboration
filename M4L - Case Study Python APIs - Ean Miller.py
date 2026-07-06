# The Book class represents a single book entry in our "API".
# Each Book has:
#   - id: a unique identifier to easily identify duplicates if accidentally added
#   - book_name: the title of the book
#   - author
#   - publisher
# Which is all the information required for the excercise.
# ------------------------------------------------------------
class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

    def __repr__(self):
        # This returns a string representation for readability when printing.
        return f"{self.id}: {self.book_name} | {self.author} | {self.publisher}"


# "Database" Storage
# ------------------------------------------------------------
# Instead of storing books in a real database, we'll use a simple list to hold our Book objects.
# This is done assuming that we weren't actually intended to use a database for this exercise or an external storage system.
# ------------------------------------------------------------
books = []

# CREATE Operation
# ------------------------------------------------------------
# Purpose:
#   Adds a new Book object to our storage list.
#
# Parameters:
#   id, name, author, publisher — all required to build a Book.
#
# Returns:
#   The newly created Book object.
# ------------------------------------------------------------
def create_book(id, name, author, publisher):
    book = Book(id, name, author, publisher)
    books.append(book)
    return book

# READ Operation
# ------------------------------------------------------------
# Retrieves a Book object by its id by looping through the list of books and 
# returning the one that matches the requested id. If none match, returns None.
# ------------------------------------------------------------
def read_book(id):
    for b in books:
        if b.id == id:
            return b
    return None  # Book not found

# UPDATE Operation
# ------------------------------------------------------------
# Modifies an existing Book object. First retrieves the book using read_book().
# Then updates only the fields that were provided.
# Note:
#   - If the book doesn't exist, returns None.
#   - Optional parameters allow partial updates.
# ------------------------------------------------------------
def update_book(id, name=None, author=None, publisher=None):
    book = read_book(id)
    if book is None:
        return None  # Cannot update something that doesn't exist

    # Only update fields that were actually passed in
    if name is not None:
        book.book_name = name
    if author is not None:
        book.author = author
    if publisher is not None:
        book.publisher = publisher

    return book

# DELETE Operation
# ------------------------------------------------------------
# Removes a Book object from storage based on its id.
# Rebuilds the list, excluding the book with the matching id.
# ------------------------------------------------------------
def delete_book(id):
    global books
    books = [b for b in books if b.id != id]


# Demonstration of the program's functionality
# ------------------------------------------------------------

# CREATE
create_book(1, "Dune", "Frank Herbert", "Chilton Books")
create_book(2, "1984", "George Orwell", "Secker & Warburg")

print("All Books:")
for b in books:
    print(b)

# READ
print("\nRead Book 1:")
print(read_book(1))

# UPDATE
print("\nUpdate Book 2:")
update_book(2, author="G. Orwell")
for b in books:
    print(b)

# DELETE
print("\nDelete Book 1:")
delete_book(1)
for b in books:
    print(b)