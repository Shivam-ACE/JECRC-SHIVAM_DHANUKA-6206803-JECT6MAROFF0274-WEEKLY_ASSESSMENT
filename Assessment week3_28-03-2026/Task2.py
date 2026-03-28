# ## Task 2
#
# ### Vogue.in automation using python selenium
#
# 1. Navigate to https://www.vogue.in/
# 2. Click on `Shopping` category
# 3. Scroll to `Olive Crest (Wings)` product and click on it
# 4. New tab opens switch to the new window
# 5. Fetch me the {name:price}

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.vogue.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Shopping"]'))).click()

ele = wait.until(EC.visibility_of_element_located((By.ID, '69845cc157840edfb23334e7')))

actions.scroll_to_element(ele).perform()
sleep(2)

ele.click()

all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])

prod_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[@class="product-title title mb-0 h2"]'))).text
prod_price = wait.until(EC.visibility_of_element_located((By.XPATH, '(//span[@class="money buckscc-money"])[1]'))).text

print(prod_name, ":", prod_price)

driver.quit()