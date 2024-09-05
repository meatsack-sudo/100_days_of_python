from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
web_form_url = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_form_url)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# print(article_count.text.split(" ")[0])

#Find element by link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the search <input> by name
# search = driver.find_element(By.NAME, value="search")
#Sending keystrokes
# search.send_keys("Python", Keys.ENTER)

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Alex", Keys.TAB)

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("England", Keys.TAB)

email = driver.find_element(By.NAME, value="email")
email.send_keys("test@email.com")

sign_up = driver.find_element(By.CLASS_NAME, value="btn")
sign_up.click()

#driver.quit()