from flask import Flask, render_template
import random
import time
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/f6c459523f05a2ee8927")


@app.route('/')
def home():
    all_blogs = response.json()
    return render_template('index.html', all_blogs=all_blogs)

@app.route('/blog/<blog_id>')
def blog_post(blog_id):
    all_blogs = response.json()
    for blog in all_blogs:
        if int(blog["id"]) == int(blog_id):
            send_blog = blog

    return render_template('post.html', blog_id=blog_id, send_blog=send_blog)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
