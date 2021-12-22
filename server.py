from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(1, 9)
print(rand_num)


@app.route('/')
def start_guessing_game():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.gif'>"


@app.route('/<int:users_number>')
def check_users_num(users_number):
    if users_number == rand_num:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media4.giphy.com/media/eaeE9qEHKUZX2/200w.webp?cid" \
               "=ecf05e47vpz8gkuqyjfmcdt7j1lvtrxwk1cmqxaewzrurndf&rid=200w.webp&ct=g' width=500> "
    elif users_number > rand_num:
        return "<h1 style='color: blue'>Too high! Try again.</h1>" \
               "<img src='https://media3.giphy.com/media/iqzp1pBJtNQUU/200w.webp?cid" \
               "=ecf05e47ypqpr83jdv5uct3kwmoqvm4oi91wdtsvnsf7c7rt&rid=200w.webp&ct=g' width=500> "
    else:
        return "<h1 style='color: red'>Too low! Try again.</h1>" \
               "<img src='https://media.giphy.com/media/XKvNduSwo0nEXsjZAg/giphy.gif' width=500>"
