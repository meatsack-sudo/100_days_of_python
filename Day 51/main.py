from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedTwitterBot import Speedtestandtweet

PROMISED_DOWN = 150
PROMISED_UP = 10

speedtest = Speedtestandtweet(PROMISED_UP, PROMISED_DOWN)

CHROME_DRIVER_PATH = "/Users/angela/Development/chromedriver"

speedtest_url = "https://www.speedtest.net/"
chrome_options = webdriver.ChromeOptions

speedtest.get_internet_speed()
speedtest.tweet_at_myconsole()

