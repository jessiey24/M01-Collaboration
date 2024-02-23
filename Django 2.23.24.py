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
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Retrieve published blog posts sorted by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # Pass the 'posts' QuerySet to the template context
    return render(request, 'blog/post_list.html', {'posts': posts})

<!-- blog/post_list.html -->

{% extends 'blog/base.html' %}

{% block content %}
  <div class="content">
    <h1>Blog Post List</h1>
    {% for post in posts %}
      <div>
        <p>Published Date: {{ post.published_date }}</p>
        <h2>{{ post.title }}</h2>
        <p>{{ post.text }}</p>
      </div>
    {% endfor %}
  </div>
{% endblock %}
# blog/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Retrieve published blog posts sorted by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Pass the 'posts' QuerySet to the template context
    return render(request, 'blog/post_list.html', {'posts': posts})
<!-- blog/templates/blog/post_list.html -->
{% extends 'blog/base.html' %}

{% block content %}
  <div class="content">
    <h1><a href="/">Django Girls Blog</a></h1>
    
    {% for post in posts %}
      <article>
        <time>published: {{ post.published_date }}</time>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
      </article>
    {% endfor %}
  </div>
{% endblock %}
python manage.py runserver
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <header class="page-header">
            <div class="container">
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
        </header>

        <main class="container">
            <div class="row">
                <div class="col">
                    {% for post in posts %}
                        <article class="post">
                            <time class="date">{{ post.published_date }}</time>
                            <h2><a href="">{{ post.title }}</a></h2>
                            <p>{{ post.text|linebreaksbr }}</p>
                        </article>
                    {% endfor %}
                </div>
            </div>
        </main>
    </body>
</html>
/* blog/static/css/blog.css */
.page-header {
    background-color: #C25100;
    margin-top: 0;
    margin-bottom: 40px;
    padding: 20px 20px 20px 40px;
}

.page-header h1,
.page-header h1 a,
.page-header h1 a:visited,
.page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

h1,
h2,
h3,
h4 {
    font-family: 'Lobster', cursive;
}

.date {
    color: #00CED1;  /* Turquoise color for the date */
}

.save {
    float: right;
}

.post-form textarea,
.post-form input {
    width: 100%;
}

.top-menu,
.top-menu:hover,
.top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h2 a,
.post h2 a:visited {
    color: #000000;
}

.post > .date,
.post > .actions {
    float: right;
}

.btn-secondary,
.btn-secondary:visited {
    color: #C25100;
    background: none;
    border-color: #C25100;
}

.btn-secondary:hover {
    color: #FFFFFF;
    background-color: #C25100;
}
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext">
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <header class="page-header">
            <div class="container">
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
        </header>
        <main class="container">
            <div class="row">
                <div class="col">
                    {% block content %}
                    {% endblock %}
                </div>
            </div>
        </main>
    </body>
</html>
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <article class="post">
            <time class="date">
                {{ post.published_date }}
            </time>
            <h2><a href="">{{ post.title }}</a></h2>
            <p>{{ post.text|linebreaksbr }}</p>
        </article>
    {% endfor %}
{% endblock %}
