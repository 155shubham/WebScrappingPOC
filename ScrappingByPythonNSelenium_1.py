from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

website = 'https://adamchoi.co.uk/overs/detailed'

# To keep the selenium browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Load the selenium chrome driver and open the website
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

web_element = driver.find_element(
    by=By.XPATH, value='//label[@analytics-event="All matches"]')
web_element.click()

# driver.quit()
