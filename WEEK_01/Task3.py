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