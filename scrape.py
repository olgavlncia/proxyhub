import requests
import os

SOURCES = {
    "http": [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    ],
    "socks4": [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://github.com/roosterkid/openproxylist/raw/refs/heads/main/SOCKS4_RAW.txt",
    ],
    "socks5": [
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://github.com/roosterkid/openproxylist/raw/refs/heads/main/SOCKS5_RAW.txt",
    ]
}

OUTPUT_DIR = "output"

def fetch_proxies():
    all_proxies = {"http": [], "socks4": [], "socks5": []}
    for proto, urls in SOURCES.items():
        for url in urls:
            try:
                print(f"📥 Fetching {proto.upper()} from {url}")
                res = requests.get(url, timeout=10)
                res.raise_for_status()
                proxies = [line.strip() for line in res.text.splitlines() if line.strip()]
                all_proxies[proto].extend(proxies)
                print(f"✅ {len(proxies)} proxies fetched.")
            except Exception as e:
                print(f"⚠️ Failed to fetch from {url}: {e}")
    return all_proxies

def save_proxies(proxies):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(f"{OUTPUT_DIR}/http.txt", "w") as f:
        f.write("\n".join(proxies["http"]))
    with open(f"{OUTPUT_DIR}/socks4.txt", "w") as f:
        f.write("\n".join(proxies["socks4"]))
    with open(f"{OUTPUT_DIR}/socks5.txt", "w") as f:
        f.write("\n".join(proxies["socks5"]))

    with open(f"{OUTPUT_DIR}/all.txt", "w") as f:
        combined = proxies["http"] + proxies["socks4"] + proxies["socks5"]
        f.write("\n".join(combined))

    print("📦 [DONE] Proxies saved to output folder.")

if __name__ == "__main__":
    proxies = fetch_proxies()
    save_proxies(proxies)
