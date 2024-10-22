from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        new_string = f"<b>{func()}</b>"
        return new_string
    return wrapper

def make_italic(func):
    def wrapper():
        new_string = f"<em>{func()}</em>"
        return new_string
    return wrapper

def make_underline(func):
    def wrapper():
        new_string = f"<u>{func()}</u>"
        return new_string
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center"> Hello World </h1>' \
    "<p> I'm a paragraph </p>" \
    '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm9ldjMwaDI2anppNDUxaGJ1ZDA4YWVjbXFlZ25yZDdkcmU5bnp3MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/21PeokB8uIQvjIhVO5/giphy.gif">'

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def say_bye():
    return "Bye"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/multi/<name>/<int:number>")
def multi_variable(name, number):
    return f"Hello {name}, you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)