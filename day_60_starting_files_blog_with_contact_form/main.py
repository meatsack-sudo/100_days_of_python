from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/Meatsack/Desktop/python training/100_days_of_python/Day 47/.env")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def send_email(to_email, subject, body, from_email, password):
    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the email body to the MIME message
    msg.attach(MIMEText(body, 'plain'))
    
    # Set up the SMTP server
    server = smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587)
    server.connect()
    server.starttls()  # Secure the connection
    server.login(to_email, password)  # Login to your email account
    
    # Send the email
    server.send_message(msg)
    
    # Close the SMTP server
    server.quit()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)
        submit_pressed = True

        to_email = os.getenv("EMAIL_ADDRESS")
        from_email = "python_price_tracker@dev.com"
        password = os.getenv("EMAIL_PASSWORD")
        subject = (f"Contact form: {name}")
        body = (f"Message sent from: {name}\n Email: {email}\n Phone: {phone}\n Message: {message}")
        send_email(to_email, subject, body, from_email, password)

        return render_template("contact.html", submit_pressed=submit_pressed)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-successful")
def form_successful():
    return render_template("form_successful.html")


def send_email(to_email, subject, body, from_email, password):
    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the email body to the MIME message
    msg.attach(MIMEText(body, 'plain'))
    
    # Set up the SMTP server
    server = smtplib.SMTP(os.getenv("SMTP_ADDRESS"), 587)
    server.connect()
    server.starttls()  # Secure the connection
    server.login(to_email, password)  # Login to your email account
    
    # Send the email
    server.send_message(msg)
    
    # Close the SMTP server
    server.quit()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
