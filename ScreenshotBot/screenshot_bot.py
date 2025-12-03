import schedule
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URLS = [
    "https://example.com",
    "https://example.com/dashboard",
    "https://example.com/analytics"
]

SAVE_PATHS = "screenshots/"

def take_screenshot(url):
    """Opens the URL & takes screenshot."""
    print(f"[+] Taking screenshot of {url}")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_url = url.replace("https://", "").replace("http://", "").replace("/", "_")
    filename = f"{SAVE_PATHS}{safe_url}_{timestamp}.png"

    driver.save_screenshot(filename)
    driver.quit()

    print(f"[✔] Saved: {filename}")

def job():
    """Run screenshot job for all URLs."""
    print("\n=== Running Scheduled Screenshot Job ===")
    for url in URLS:
        take_screenshot(url)
    print("=== Job Completed ===\n")


schedule.every(1).hours.do(job)

print("Screenshot bot started. Taking screenshots every hour.")

while True:
    schedule.run_pending()
    time.sleep(1)