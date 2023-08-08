import os
import requests
import csv
from urllib.parse import urlparse
from selenium import webdriver

# Read URLs from url.txt
with open("url.txt", "r") as file:
    urls = file.read().splitlines()

# Create a folder for screenshots
if not os.path.exists("poc"):
    os.makedirs("poc")

# Set up Chrome webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Prepare CSV file
csv_file = "status.csv"
with open(csv_file, "w", newline="") as csvf:
    csv_writer = csv.writer(csvf)
    csv_writer.writerow(["URL", "Status Code"])

# Loop through the URLs
for url in urls:
    try:
        # Check if URL starts with http or https
        if url.startswith("http://") or url.startswith("https://"):
            response = requests.get(url)
            status_code = response.status_code
            
            # Capture screenshot if status code is 200, 301, or 302
            if status_code in [200, 301, 302]:
                parsed_url = urlparse(url)
                url_name = parsed_url.netloc.replace(".", "_")
                screenshot_path = os.path.join("poc", f"{url_name}.png")
                
                # Open URL and capture screenshot
                driver.get(url)
                driver.save_screenshot(screenshot_path)
                
                print(f"Screenshot captured for {url}")
            else:
                print(f"Skipping {url} due to status code {status_code}")
            
            # Write status to CSV file
            with open(csv_file, "a", newline="") as csvf:
                csv_writer = csv.writer(csvf)
                csv_writer.writerow([url, status_code])
                
        else:
            print(f"Skipping {url} as it doesn't start with 'http://' or 'https://'")

    except Exception as e:
        print(f"Error capturing screenshot for {url}: {e}")

# Close the Chrome webdriver
driver.quit()
print("Screenshots and status information saved.")
