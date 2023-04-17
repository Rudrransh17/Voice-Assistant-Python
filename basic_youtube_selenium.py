import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def PlayYoutube(input):
    query = input.split(' ',1)[1]
    browser = webdriver.Chrome() # Opens chrome browser
    browser.maximize_window()
    # Goes to following URL
    browser.get('http://www.youtube.com/')
    # Create the search box object
    search_box = browser.find_element("name", "search_query")
	# Type what to search as key
    search_box.send_keys(query)
	# Submit the search
    search_box.submit()
    time.sleep(5)
    # Find song element
    xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"
    card = browser.find_element(By.XPATH,xpath)
    card.click()
    time.sleep(10)
   

PlayYoutube('play shape of you')