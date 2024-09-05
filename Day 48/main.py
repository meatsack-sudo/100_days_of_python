from selenium import webdriver
from selenium.webdriver.common.by import By

amazon_url = "https://www.amazon.com/ASUS-Gaming-GeForce-Graphics-DisplayPort/dp/B0C7JYX6LN/ref=sr_1_1?crid=27EYH938UEWXE&dib=eyJ2IjoiMSJ9.cg3WemZyp1JKr40TslHazvK9wE7E9TuEw-MKqYI1BO0Oj9XOrXwMkfwjRFROcHT9y_Ft6c3t6oz3yQlPzZC8xvaKjoh40OgiLMPX9I_7RTP3os9FtUUy5UVOkxXRPhsN0yXqJhITVehtcGyiKINZPbXyuZJsfqsjU93GwLOsC6mcaQIE2AvkrlPeub8bdaMgj_tfvw1XiKnrKcxmB3JZmXMy562bhryAHbLkmw4NFrU.0IuvbSeZdR0T1MVjmmGr5w-EKEyAM3RssxTQRJi0PTA&dib_tag=se&keywords=4090&qid=1724970338&sprefix=4090%2Caps%2C96&sr=8-1"
python_org_url = "https://www.python.org/"
#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(python_org_url)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}. ")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

#button = driver.find_element(By.ID, value="submit")
#print(button.size)

# price = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# print(price.text)

# #Locate the elements
# python_events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

# # Initialize an empty list and dictionary
# list_of_events = []
# dict_of_events = {}

# count = 0

# # Initialize an empty dictionary
# dict_of_events = {}

# # Iterate over each event element
# for e in python_events:
#     event_text = e.text.split('\n')  # Split by newline to separate date and event name
#     date = event_text[0]
#     event_name = event_text[1]
    
#     # Append the event name and date to the dictionary with the current count as the key
#     dict_of_events[count] = {'Date': date, 'Event-Title': event_name}
    
#     count += 1


event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

# Print the dictionary of events
# print(dict_of_events)


#print(python_events)
#print(list_of_events)
#driver.close() --Closes the tab
driver.quit() #--Closes the application

# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]