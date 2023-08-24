from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def scrape_table_data():
    """Scrape the table data from the ISCC website."""

    weburl = "https://www.iscc-system.org/certification/certificate-database/all-certificates/"
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(weburl)
    driver.maximize_window()

    driver.implicitly_wait(10)

    nextpage_no_xpath = "//span/a[@class='paginate_button '][@data-dt-idx='4']"
    nextpage_no_element = driver.find_element(
        by=By.XPATH, value=nextpage_no_xpath)

    if nextpage_no_element is not None:
        # print(nextpage_no_element)
        nextpage_no_element.click()
    else:
        print('Not found: %s', nextpage_no_element)

    driver.implicitly_wait(10)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("table", {"id": "table_1"})

    data = []
    if table is not None:
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            data.append([col.text for col in cols])
    else:
        print("Table not found on this page")

    driver.close()
    return data


def main():
    """Scrape the table data and create a JSON file."""
    data = scrape_table_data()
    # create_json_file(data)
    print(data)


if __name__ == "__main__":
    main()
