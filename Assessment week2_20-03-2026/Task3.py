# ## Task 3
#
# ### Automation script for google.com
#
# Open Google
#
# Enter "Selenium Python"
#
# Use explicit wait for suggestions
#
# Capture all suggestions using find_elements
#
# Print them
#
# Click one suggestion

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search = wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))
search.send_keys("Selenium Python")

suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="Alh6id"]/div//li')))
for suggestion in suggestions:
    print(suggestion.text)

suggestions[9].click()

driver.quit()