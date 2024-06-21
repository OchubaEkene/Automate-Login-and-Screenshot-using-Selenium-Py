# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import os
from dotenv import load_dotenv
import time
from PIL import Image

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
]

# Randomly select a user agent
user_agent = random.choice(user_agents)

# Locate Webdriver
driver_path = r'C:\Users\Tester\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Optional argument, if not specified will search path.
service = Service(driver_path)

# Create an Options object and set the user agent
options = Options()
options.add_argument(f"user-agent={user_agent}")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to URL
    driver.get('https://auth.geeksforgeeks.org/')

    # Maximize Window
    driver.maximize_window()
    time.sleep(5)

    # Find elements and input credentials
    load_dotenv()
    username = os.getenv('NAME')
    password = os.getenv('PASSWORD')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'luser'))).send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(3)

    # Click Login button
    driver.find_element(By.CLASS_NAME, 'btn-green').click()  # Assuming 'btn-green' is unique
    time.sleep(10)

    # Escape Pop-up if present
    try:
        pop_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'lower_section_text')))
        if pop_up:
            pop_up.click()
    except:
        pass
    time.sleep(10)

    print('Time to Screenshot!')

    # Get the total height of the page
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    screenshots = []
    for i in range(0, total_height, viewport_height):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(2)  # Wait for scrolling to finish
        screenshot_path = f'part_{i}.png'
        driver.save_screenshot(screenshot_path)
        screenshots.append(screenshot_path)

    # Stitch screenshots together
    full_image = Image.new('RGB', (driver.execute_script("return window.innerWidth"), total_height))
    y_offset = 0
    for screenshot in screenshots:
        img = Image.open(screenshot)
        full_image.paste(img, (0, y_offset))
        y_offset += img.height
        os.remove(screenshot)  # Remove part screenshot after stitching

    full_screenshot_path = 'picture/full_screenshot.png'
    os.makedirs(os.path.dirname(full_screenshot_path), exist_ok=True)
    full_image.save(full_screenshot_path)
    print('Full-page screenshot taken!')

finally:
    # Close Window
    driver.quit()
