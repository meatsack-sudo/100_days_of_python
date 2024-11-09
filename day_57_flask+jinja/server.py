from flask import Flask, render_template
import random
import time
import requests



app = Flask(__name__)

@app.route('/')
def home():
    current_year = time.strftime("%Y")
    random_number = random.randint(1, 10)
    return render_template('index.html', random_number=random_number, current_year=current_year)

@app.route("/guess/<string:name>")
def guess(name):
    gender_respone = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_respone.json()
    gender_text = gender_respone.text
    print(gender_text)

    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()
    age_text = age_response.text
    print(age_text)

    return render_template('agify.html', gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blogs = response.json()

    return render_template('blog.html', all_blogs=all_blogs)

if __name__ == "__main__":
    app.run(debug=True)

    