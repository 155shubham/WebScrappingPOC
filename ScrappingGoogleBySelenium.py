from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# Create a WebDriver instance.
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

# Navigate to a web page.
driver.get("https://www.google.com")

# Enter a search query.
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Selenium")

# Click the search button.
search_button = driver.find_element(by=By.NAME, value="btnK")
search_button.click()

# Get the search results.
results = driver.find_element(by=By.CLASS_NAME, value="g")

# Print the search results.
for result in results:
    print(result.text)

# Close the web browser.
driver.close()
