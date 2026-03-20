#Write a Selenium script that opens multiple websites sequentially, including a few e-commerce sites [souled store, nike... any], a news website, and the official Python website. The script should wait for 3 seconds before opening and later should print the title of each page. finally close the browser.  

from selenium import webdriver
import time

websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com",
    "https://www.python.org"
]

driver = webdriver.Chrome()

for site in websites:
    time.sleep(3)

    driver.get(site)

    print("Website:", site)
    print("Page Title:", driver.title)

driver.quit()
