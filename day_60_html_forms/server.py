from flask import Flask, render_template, request
import random
import time
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def receive_data():
    print("I got mail")
    if request.method == 'POST':
        #first_name = request.form(['fname'])
        #password = request.form(['password'])

        return form_successful(request.form['fname'], request.form['password'])

@app.route('/form_submit')
def form_successful(fname, password):
    return render_template('throw_up.html', password=password, fname=fname)


if __name__ == "__main__":
    app.run(debug=True)