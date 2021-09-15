import json

from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Ivan",
        "age": 34,
        "is_blocked": False
    },
    {
        "id": 2,
        "name": "Peter",
        "age": 23,
        "is_blocked": True
    }
]


@app.route('/books')
def books():
    with open('books.json') as f:
        data = json.load(f)
        return ???


if __name__ == '__main__':
    app.run()
