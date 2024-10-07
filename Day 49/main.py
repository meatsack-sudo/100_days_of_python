from selenium import webdriver
from selenium.webdriver.common.by import By
import time

linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=4006411033&keywords=python%20developer&origin=BLENDED_SEARCH_RESULT_NAVIGATION_JOB_CARD&originToLandingJobPostings=4006411033%2C4021594443%2C4021243762"

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(linkedin_url)

#Find sign in button and click it
try:
    sign_in_button = driver.find_element(By.CLASS_NAME, value="sign-in-modal__outlet-btn")
except:
    print("Different kind of sign in button, let's try the href one.")
    sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")

sign_in_button.click()

#lets sleep while sign in page loads
print("Waiting 5 seconds")
time.sleep(5)

#Populate our log in info
try:
    username = driver.find_element(By.ID, value="username")
except:
    username = driver.find_element(By.ID, value="base-sign-in-modal_session_key")

username.send_keys("t6587352@gmail.com")

try:
    password = driver.find_element(By.ID, value="password")
except:
    password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")

password.send_keys("26F472Rzn:!m")

#Lets sleep again while wait for forms to fill
print("Waiting 5 seconds")
time.sleep(5)

try:
    sign_in_button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
except:
    sign_in_button = driver.find_element(By.CLASS_NAME, value="sign-in-form__submit-btn--full-width")
sign_in_button.click()






