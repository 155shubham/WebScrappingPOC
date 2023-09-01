from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

website = {
    "ISCC": "https://www.iscc-system.org/certification/certificate-database/all-certificates/"}

xpaths = {
    "dropdown_button_xpath": "//*[@id='table_1_length']/label/div/button",
    "anchor_xpath": "//*[@id='table_1_length']/label/div/div/ul/li[6]/a"
}

# Navigate to the website.
driver.get(website["ISCC"])

wait = WebDriverWait(driver, 10)

# Find the dropdown button element
dropdown_button_element = driver.find_element(
    By.XPATH, xpaths["dropdown_button_xpath"])

# Wait for the element to become visible
wait.until(EC.visibility_of(dropdown_button_element))
dropdown_button_element.click()
# time.sleep(5)

# Find the dropdown button element
wait.until(EC.element_to_be_clickable(
    (By.XPATH, xpaths["anchor_xpath"]))).click()

print("completed")

time.sleep(5)
