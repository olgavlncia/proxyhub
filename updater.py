import os
import requests

SOURCES = {
    "http": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt"
    ],
    "socks4": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"
    ],
    "socks5": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
    ]
}

def fetch_proxies(urls):
    proxies = set()
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                for line in res.text.strip().splitlines():
                    if line and ':' in line:
                        proxies.add(line.strip())
        except Exception as e:
            print(f"[!] Failed to fetch from {url}: {e}")
    return proxies

def save_output(protocol, proxy_list):
    os.makedirs("output", exist_ok=True)
    path = f"output/{protocol}.txt"
    with open(path, "w") as f:
        f.write("\n".join(sorted(proxy_list)))
    print(f"[+] Saved {len(proxy_list)} {protocol.upper()} proxies to {path}")

if __name__ == "__main__":
    for proto, urls in SOURCES.items():
        print(f"[*] Fetching {proto.upper()} proxies...")
        proxies = fetch_proxies(urls)
        save_output(proto, proxies)
