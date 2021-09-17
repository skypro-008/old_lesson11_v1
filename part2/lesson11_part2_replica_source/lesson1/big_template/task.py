import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/prizes')
def phones():
    prices = [1300, 400, 100]
    user = {
        "blocked": False
    }
    prize_name = "Flight Ticket"

    return render_template("/prizes.html", prices=prices, user=user, prize_name=prize_name)


if __name__ == '__main__':
    app.run()
