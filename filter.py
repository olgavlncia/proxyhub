import asyncio
import aiohttp
import os

# Konfigurasi
TEST_URL = "https://httpbin.org/ip"
TIMEOUT = 10
CONCURRENT = 100  # jumlah request paralel

INPUT_DIR = "output"
OUTPUT_DIR = "output/active"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Baca proxy dari file
def load_proxies(file_path, prefix):
    with open(file_path, "r") as f:
        return [f"{prefix}://{line.strip()}" for line in f if line.strip()]

# Uji koneksi proxy
async def test_proxy(session, proxy):
    try:
        async with session.get(TEST_URL, proxy=proxy, timeout=TIMEOUT) as resp:
            if resp.status == 200:
                print(f"[✅] Live: {proxy}")
                return proxy
    except:
        pass
    return None

# Loop async untuk semua proxy
async def filter_proxies(proxies):
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for proxy in proxies:
            tasks.append(test_proxy(session, proxy))
            if len(tasks) >= CONCURRENT:
                results = await asyncio.gather(*tasks)
                for r in results:
                    if r: yield r
                tasks = []

        # Sisa
        if tasks:
            results = await asyncio.gather(*tasks)
            for r in results:
                if r: yield r

# Main logic per protocol
async def process_protocol(protocol):
    file_map = {
        "http": ("http.txt", "http"),
        "socks4": ("socks4.txt", "socks4"),
        "socks5": ("socks5.txt", "socks5")
    }

    input_file, prefix = file_map[protocol]
    proxies = load_proxies(os.path.join(INPUT_DIR, input_file), prefix)

    print(f"🔍 Testing {len(proxies)} {protocol} proxies...")
    alive = []
    async for working in filter_proxies(proxies):
        alive.append(working)

    # Save result
    out_path = os.path.join(OUTPUT_DIR, input_file)
    with open(out_path, "w") as f:
        f.write("\n".join([p.split("://")[1] for p in alive]))
    print(f"[💾] {len(alive)} aktif → {out_path}")

async def main():
    for proto in ["http", "socks4", "socks5"]:
        await process_protocol(proto)

if __name__ == "__main__":
    asyncio.run(main())
