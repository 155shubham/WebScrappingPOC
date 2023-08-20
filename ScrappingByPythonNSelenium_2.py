from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the webdriver (make sure you have the appropriate webdriver executable)
driver = webdriver.Chrome()  # Change to the appropriate webdriver for your browser
url = "https://www.iscc-system.org/certification/certificate-database/all-certificates/"
driver.get(url)

# Wait for the page to load, you might need to adjust the waiting time
driver.implicitly_wait(10)

# Get the HTML content
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Find the table
table = soup.find("table", {"id": "certificate-table"})

# Initialize a list to store the data
data = []

# Iterate through rows in the table
if table is not None:
    for row in table.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td")
        certificate_number = columns[0].text.strip()
        holder = columns[1].text.strip()
        country = columns[2].text.strip()
        # You can add more columns as needed

        data.append({
            "certificate_number": certificate_number,
            "holder": holder,
            "country": country
            # Add more key-value pairs for additional columns
        })
else:
    print("Table not found on this page")

# Print the data
print(data)

# Close the driver
driver.quit()
