from flask import Flask
import math
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Guess a number between 0 and 9</p>" \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(0, 9)
print(random_number)

@app.route("/guessed_number/<int:number>")
def guessed_number_page(number):
    if number == random_number:
        return f"<p><b>You were correct!!!!</b></p>" \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number > random_number:
        return f"<p><b>Your number was too high.</b></p>" \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f"<b><p>Your number was too low.</p></b>" \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    


if __name__ == "__main__":
    app.run(debug=True)