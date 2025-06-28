import time
import os

def run_all():
    os.system("python scrape.py")
    os.system("python filter.py")
    os.system("python geo.py")
    os.system("python convert_to_csv.py")

while True:
    print("🔁 Mulai siklus ProxyHub...")
    run_all()
    print("✅ Siklus selesai. Tidur 15 menit...\n")
    time.sleep(900)
