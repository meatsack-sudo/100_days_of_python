from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Speedtestandtweet:

    def __init__(self, up, down):
        self.speedtest_url = "https://www.speedtest.net/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = up
        self.down = down


    def get_internet_speed(self):
        self.driver.get(self.speedtest_url)
        #Lets give the site a chance to load. Lot of ads on site so takes a sec.
        print("Sleeping for 10 seconds while the page loads.")
        time.sleep(10)
        start_test = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        start_test.click()
        #Wait 40 seconds for test to finish
        print("Waiting for 40 seconds while test runs.")
        time.sleep(40)
        self.result_down = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        self.result_up = self.driver.find_element(By.CLASS_NAME, value="upload-speed")

    def tweet_at_myconsole(self):
        print(f"Download speed is: {self.result_down.text}. Upload speed is: {self.result_up.text}.")
        
        if float(self.result_up.text) < (self.up - (self.up * 0.10)):
            print("You're upload speed is lower than what you should be getting by greater than 10%")
        if float(self.result_down.text) < (self.down - (self.down * 0.10)):
            print("You're download speed is lower than what you should be getting by greater than 10%")
            
