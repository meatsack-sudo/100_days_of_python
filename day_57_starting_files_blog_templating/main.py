from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)

@app.route('/')
def home():
    all_blogs = response.json()

    return render_template("index.html", all_blogs=all_blogs)

@app.route('/blog/<blog_id>')
def blog_post(blog_id):
    all_blogs = response.json()
    for blog in all_blogs:
        if int(blog["id"]) == int(blog_id):
            send_blog = blog

    return render_template("post.html", blog_id=blog_id, send_blog=send_blog)

if __name__ == "__main__":
    app.run(debug=True)
