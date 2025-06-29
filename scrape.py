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
        print(f"\n🔎 Fetching {proto.upper()} proxies...")
        for url in urls:
            try:
                res = requests.get(url, timeout=10)
                res.raise_for_status()
                lines = [line.strip() for line in res.text.splitlines() if ":" in line]
                all_proxies[proto].extend(lines)
                print(f"  ✅ {len(lines)} proxies from {url}")
            except Exception as e:
                print(f"  ⚠️  Failed to fetch from {url} → {e}")
    return all_proxies

def save_proxies(proxies):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    def write_file(name, data):
        path = os.path.join(OUTPUT_DIR, name)
        with open(path, "w") as f:
            f.write("\n".join(sorted(set(data))))
        print(f"💾 Saved {len(data)} → {path}")

    write_file("http.txt", proxies["http"])
    write_file("socks4.txt", proxies["socks4"])
    write_file("socks5.txt", proxies["socks5"])
    write_file("all.txt", proxies["http"] + proxies["socks4"] + proxies["socks5"])

    print("\n✅ All proxies saved successfully.")

if __name__ == "__main__":
    proxies = fetch_proxies()
    save_proxies(proxies)
