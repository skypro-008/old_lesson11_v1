import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/phones')
def phones():
    phones = [
        {
            "name": "Ivan",
            "mail": "ivan@mail.ru",
            "phone": "89991234567"
        },
        {
            "name": "Maxim",
            "mail": "maxim@mail.ru",
            "phone": "89991234567"
        },
        {
            "name": "Peter",
            "mail": "maxim@mail.ru",
            "phone": "89991234567"
        }
    ]

    return render_template("/phones.html", phones=phones)


if __name__ == '__main__':
    app.run()
