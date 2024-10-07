from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

def returnN(string, length):
    return string[:length] if len(string) >= length else ''

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zillow_url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

properties_list = []

properties = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
properties_links = soup.find_all('a', class_="property-card-link")
properties_cost = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

for x in range(0, len(properties_cost)):

    cost = returnN(properties_cost[x].get_text(strip=True).replace("$", "").replace(",", ""), 4)
    address = properties[x].get_text(strip=True).split("$")[0]
    link = properties_links[x].get('href')

    properties_list.append({
        "cost" : cost,
        "address" : address,
        "link" : link
    })

#print(properties_list)

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfNGtjPrVhxQjYMdFK0e3KQrPNxoJAVPa-joHhiR3xjyMSiHg/viewform"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_url)
time.sleep(5)

#address.send_keys(properties_list[1]["address"])
# price.send_keys("test")
# property_link.send_keys("test")

for x in range(len(properties_list)):
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address.send_keys(properties_list[x]["address"])

    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price.send_keys(properties_list[x]["cost"])

    property_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    property_link.send_keys(properties_list[x]["link"])
    time.sleep(1)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    time.sleep(1)

    new_response_button = driver.find_element(By.LINK_TEXT, value="Submit another response")
    new_response_button.click()
    time.sleep(1)


#print(properties)