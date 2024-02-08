from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace this with a database later)
books = [
    {"id": 1, "book_name": "Sample Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Sample Book 2", "author": "Author 2", "publisher": "Publisher 2"},
]

# CRUD operations
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify(updated_book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
