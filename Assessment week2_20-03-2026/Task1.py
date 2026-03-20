'''## Task 1

### Automation script for amazon.com

Open Amazon

Verify page title and current URL

Locate the category dropdown (next to search bar)

Select "Books" using Select class

Enter "Harry Potter" in search and press Enter

Use explicit wait to wait until results are visible

Get all product titles using find_elements

Print first 5 product names

Click on the first product'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.amazon.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

print("Title:", driver.title)
print("URL:", driver.current_url)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue shopping"]'))).click()
except:
    pass

dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox"))))
dropdown.select_by_visible_text("Books")

search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("Harry Potter", Keys.ENTER)

products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")))

print("\nTop 5 Products:")
for i in range(5):
    print(products[i].text)

wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-component-type='s-search-result']//h2//span)[1]"))).click()

driver.quit()