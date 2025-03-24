from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
import os

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)
service = Service("path/to/chromedriver")  # Specify your chromedriver path
driver = webdriver.Chrome(service=service, options=options)

# Google Image Search URL
search_query = "stars in the night sky"
driver.get(f"https://www.google.com/search?tbm=isch&q={search_query.replace(' ', '+')}")

# Wait for images to load
time.sleep(3)

# Extract image elements
images = driver.find_elements(By.CSS_SELECTOR, "img")

# Create folder to save images
save_folder = "star_images"
os.makedirs(save_folder, exist_ok=True)

# Download images
for i, img in enumerate(images[:5]):  # Limit to first 5 images
    img_url = img.get_attribute("src")
    if img_url and "http" in img_url:
        img_data = requests.get(img_url).content
        with open(os.path.join(save_folder, f"star_image_{i+1}.jpg"), "wb") as f:
            f.write(img_data)
        print(f"Downloaded: star_image_{i+1}.jpg")

# Close the browser
driver.quit()
