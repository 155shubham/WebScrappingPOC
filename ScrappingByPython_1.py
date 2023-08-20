import requests
from bs4 import BeautifulSoup
import json


def scrape_table_data():
    """Scrape the table data from the ISCC website."""

    url = "https://www.iscc-system.org/certification/certificate-database/all-certificates/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # table = soup.find(
    #     "table", id="table_1", class_="responsive display nowrap data-t data-t wpDataTable wpDataTableID-2 dataTable")

    table = soup.find("table", {"id": "table_1"})

    print(table)

    data = []
    if table is not None:
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            data.append([col.text for col in cols])
    else:
        print("Table not found on this page")

    return data


def create_json_file(data):
    """Create a JSON file from the scraped data."""

    json_data = json.dumps(data, indent=4)

    with open("iscc_certificates.json", "w") as f:
        f.write(json_data)


def main():
    """Scrape the table data and create a JSON file."""

    data = scrape_table_data()
    create_json_file(data)


if __name__ == "__main__":
    main()
