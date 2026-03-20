# ---
#
# ## Task 2
#
# ### Automation script for the following
#
# Open signup page `https://automationexercise.com/signup`
#
# Enter name & email
#
# Select Title (Mr/Mrs) → Radio button
#
# Select checkboxes:
# `Newsletter`
# `Special offers`
#
# Use get_attribute("checked") to verify selection
#
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")
driver.get("https://automationexercise.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH, '(//ul[@class="nav navbar-nav"]/li)[4]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Name"]'))).send_keys("ABC")
wait.until(EC.presence_of_element_located((By.XPATH, '(//input[@placeholder="Email Address"])[2]'))).send_keys("ghvhgvhgv@gmail.com")
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Signup"]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_gender1"]'))).click()

checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]')))
for checkbox in checkboxes:
    checkbox.click()

print('Newsletter selected:',checkboxes[0].get_attribute('checked'))
print('Special offers selected:',checkboxes[1].get_attribute('checked'))

sleep(2)

driver.quit()