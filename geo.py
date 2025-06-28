import asyncio
import aiohttp
import os
import json
from time import time

API_URL = "http://ip-api.com/json/"  # alternatif: ipwho.is, ipinfo.io

INPUT_FILE = "output/active/http.txt"
OUTPUT_FILE = "output/geo/geo_http.json"
os.makedirs("output/geo", exist_ok=True)

CONCURRENT = 50
TIMEOUT = 8

def load_proxies(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]

async def fetch_geo(session, proxy):
    proxy_url = f"http://{proxy}"
    start = time()
    try:
        async with session.get("https://api.myip.com", proxy=proxy_url, timeout=TIMEOUT) as resp:
            if resp.status != 200:
                return None
            elapsed = round((time() - start) * 1000)
            data = await resp.json()
    except:
        return None

    # Cek IP-nya pakai GeoAPI
    try:
        async with session.get(f"{API_URL}{data['ip']}?fields=status,country,query,isp") as geo:
            result = await geo.json()
            if result.get("status") == "success":
                return {
                    "ip": result.get("query"),
                    "type": "http",
                    "country": result.get("country"),
                    "isp": result.get("isp"),
                    "latency_ms": elapsed,
                    "proxy": proxy
                }
    except:
        return None

async def gather_geo(proxies):
    results = []
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for proxy in proxies:
            tasks.append(fetch_geo(session, proxy))
            if len(tasks) >= CONCURRENT:
                chunk = await asyncio.gather(*tasks)
                results.extend([r for r in chunk if r])
                tasks = []

        if tasks:
            chunk = await asyncio.gather(*tasks)
            results.extend([r for r in chunk if r])
    return results

async def main():
    proxies = load_proxies(INPUT_FILE)
    print(f"🌍 Cek lokasi {len(proxies)} proxy...")
    result = await gather_geo(proxies)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2)

    print(f"[✅] Disimpan ke {OUTPUT_FILE} ({len(result)} proxy)")

if __name__ == "__main__":
    asyncio.run(main())
