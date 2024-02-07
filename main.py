from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging

"""
Practice using selenium to access and interact with webpages
using google chrome browser
"""

logging.basicConfig(level=logging.ERROR)

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.bhphotovideo.com/c/product/1542675-REG/fujifilm_x100v_digital_camera_silver.html")


stock_element = driver.find_element(By.CLASS_NAME, "statusMedium_ZC_6IRXKyD")
status = stock_element.text

item_element = driver.find_element(By.CSS_SELECTOR, "div.title_RiltKdop13")
item = item_element.text
print ("\n" + item + ": " + status + "\n")


black_btn = driver.find_element(By.CLASS_NAME, "itemLink_Wkz432Dx46")

time.sleep(2)


black_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "itemLink_Wkz432Dx46")))

black_btn.click()


driver.quit()

