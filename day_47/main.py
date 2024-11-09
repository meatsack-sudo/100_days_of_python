from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/Meatsack/Desktop/python training/100_days_of_python/Day 47/.env")

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
    server.starttls()  # Secure the connection
    server.login(to_email, password)  # Login to your email account
    
    # Send the email
    server.send_message(msg)
    
    # Close the SMTP server
    server.quit()


amazon_url = "https://www.amazon.com/Rapink-Ethernet-Support-Snagless-Flexiable/dp/B0BXSN6ZPR/ref=pd_hp_d_btf_rpt_sd_biaws_c_1?_encoding=UTF8&dd=N2jTjsRP5USWd7iVvBSn_NNGzeC2M1AGI-JCm90QnS4%2C&ddc_refnmnt=free&pd_rd_i=B0BXSN6ZPR&pd_rd_w=CmuC7&content-id=amzn1.sym.ae3c55fc-7f19-4a1a-be25-ba2c1b81e6de&pf_rd_p=ae3c55fc-7f19-4a1a-be25-ba2c1b81e6de&pf_rd_r=6MS1MSZEHBKKFGQRW2ZA&pd_rd_wg=ekHjM&pd_rd_r=d705b9d7-15aa-4d5e-b894-b694518d750e&th=1"

response = requests.get(amazon_url, headers={"Accept-Language":"en-US", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"})
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price_text = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
price_text_clean = float(price_text.get_text(strip=True).split("$")[1])

target_price = 100

# Example usage:
to_email = os.getenv("EMAIL_ADDRESS")
from_email = "python_price_tracker@dev.com"
password = os.getenv("EMAIL_PASSWORD")
subject = "Test Email"
body = (f"The price for your tracked item has dropped below your target price of {target_price} and is currently {price_text.get_text(strip=True)}")

if price_text_clean < target_price:
    send_email(to_email, subject, body, from_email, password)


print(price_text_clean)
