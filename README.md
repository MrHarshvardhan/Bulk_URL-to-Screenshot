# Website Screenshot and Status Checker

A Python script to capture screenshots of websites and check their status codes. The script reads a list of URLs from a text file, captures screenshots for URLs with successful responses (status codes 200, 301, or 302), and saves the status information in a CSV file.

## Usage

1. Clone or download this repository.

2. Prepare a file named `url.txt` in the same directory containing the list of URLs, with each URL on a separate line.

3. Install the required Python packages using the following command: pip install requests selenium

4. Download the appropriate version of the Chrome WebDriver for your system and place it in the same directory as the script. WebDriver download: https://sites.google.com/chromium.org/driver/

5. Run the script:

6. The script will create a folder named `poc` to save the captured screenshots and generate a CSV file named `status.csv` to store the URL and status code information.

**Note**: Make sure you have Google Chrome installed on your system.

## Disclaimer

This script is provided as-is and is intended for educational and research purposes only. The author is not responsible for any misuse or damage caused by this script. Use at your own risk.

## Requirements

- Python (>= 3.6)
- Google Chrome browser
- Chrome WebDriver: Download and place in the script directory.

## Credits

- Python: https://www.python.org/
- Requests library: https://docs.python-requests.org/en/master/
- Selenium library: https://www.selenium.dev/documentation/en/
