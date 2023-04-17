import time

from selenium import webdriver



driver = webdriver.Chrome()  # Opens the browser

# Goes to following URL
driver.get('http://www.google.com/');

time.sleep(1) # Let the user actually see something!

# Create the search box object
search_box = driver.find_element("name", "q")
# Type what to search as key
search_box.send_keys('What is selenium')
# Submit the search
search_box.submit()

time.sleep(3) # Let the user actually see something!

driver.quit()