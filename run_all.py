import multiprocessing
import os
import time
from flask_app import app

def background_loop():
    while True:
        os.system("python scrape.py")
        os.system("python filter.py")
        os.system("python geo.py")
        os.system("python convert_to_csv.py")
        print("✅ Cycle done. Sleeping 15 min.")
        time.sleep(900)

def start_flask():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=background_loop)
    p2 = multiprocessing.Process(target=start_flask)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
