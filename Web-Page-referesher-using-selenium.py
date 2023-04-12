from selenium import webdriver
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage you want to refresh
driver.get("https://www.youtube.com/")

while True:
    # Wait for 20 seconds
    time.sleep(10)

    # Refresh the webpage
    driver.refresh()
