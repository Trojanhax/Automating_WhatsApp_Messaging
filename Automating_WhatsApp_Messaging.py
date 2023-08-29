from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

# Config
login_time = 50     # Time for login (in seconds)
new_msg_time = 15    # Time for a new message (in seconds)
send_msg_time = 15   # Time for sending a message (in seconds)
country_code = 91   # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
input("Scan the QR code and press Enter after login...")

# Read message content
with open('message.txt', 'r', encoding='utf-8') as file:
    msg = quote(file.read())

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = webdriver.ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()
