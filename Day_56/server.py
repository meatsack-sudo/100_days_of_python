from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')



    # return '<h1 style="text-align: center"> Hello World </h1>' \
    # "<p> I'm a paragraph </p>" \
    # '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm9ldjMwaDI2anppNDUxaGJ1ZDA4YWVjbXFlZ25yZDdkcmU5bnp3MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/21PeokB8uIQvjIhVO5/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)