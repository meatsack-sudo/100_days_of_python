from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

cookie_url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(cookie_url)

upgrades = driver.find_elements(By.ID, value="store")
upgrade_costs = []

counter = 0

for upgrade in upgrades:
    upgrade = upgrade.text.replace(",","")
    # Split the upgrade text by newlines, and for every second item (costs), clean and store it
    upgrade_details = upgrade.split("\n")
    for i in range(0, len(upgrade_details), 2):
        # Extract the cost part, remove commas, and store it
        cost = upgrade_details[i].split("-")
        upgrade_costs.append(cost)

print(upgrade_costs)
# print(int(upgrade_costs[0][-1]))
# print("\n")


def click_the_cookie():
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

def check_upgrade():
    global counter
    current_cookies = int(driver.find_element(By.ID, value="money").text.replace(",", ""))


    print(f"Current cookies are: {current_cookies}")

    for i in range(len(upgrade_costs) - 1, -1, -1):
        price = int(upgrade_costs[i][-1])
        #print(f"Price is returning as {price}")
        if int(price) < current_cookies:
            upgrade_to_buy = driver.find_element(By.ID, value=(f"buy{upgrade_costs[i][0].rstrip()}"))
            upgrade_to_buy.click()
            counter = 0
            break
        else:
            continue


#driver.quit()


start_time = time.time()
max_duration = 5 * 60

while time.time() - start_time < max_duration:

    while counter < 18:
        click_the_cookie()
        counter+=1
        
    check_upgrade()    

cookies_per_second = driver.find_element(By.ID, value="cps")
print(cookies_per_second.text)
