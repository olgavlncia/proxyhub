import os
import time

while True:
    os.system("python3 scrape.py")
    print("🔁 Scraping done. Sleeping 6 hours...")
    time.sleep(6 * 60 * 60)  # 6 jam
