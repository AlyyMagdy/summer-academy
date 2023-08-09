from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


# Create a new instance of the Chrome driver
options = Options()
options.add_experimental_option("detach",True)
# edge_driver_path = 'drivers/msedgedriver.exe'
driver = webdriver.Chrome()

# Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Find the username and password input fields and enter the credentials
username_field = driver.find_element("name", "username")
password_field = driver.find_element("name", "password")

 

username_field.send_keys("student")
password_field.send_keys("Password123")

 

# Submit the form
submit_button = driver.find_element('id', 'submit')
submit_button.click()

# Verify if login was successful
if "logged-in-successfully" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")



# Close the browser
# driver.quit()