<p align="center">
  <img src="assets/logo.gif" width="120" alt="ProxyHub Logo" />
</p>

<h1 align="center">🛰️ ProxyHub</h1>

<p align="center">
  🔌 Free Proxy Scraper · 🌍 Geo Lookup · 📄 JSON & CSV Export · ✨ Auto Update via GitHub Actions
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square">
</p>

---

## 🚀 Fitur

* Scrape HTTP / SOCKS4 / SOCKS5 dari banyak sumber
* Filter proxy aktif (async)
* GeoIP lookup & latency test
* Export ke `.json` & `.csv`
* Update otomatis (GitHub Actions)
* Public API (Flask + Railway)

---

## 📂 Hasil Proxy Siap Pakai

| Jenis          | Link                                                                               |
| -------------- | ---------------------------------------------------------------------------------- |
| 📦 Semua Proxy | [all.txt](https://github.com/aesneverhere/proxyhub/blob/main/output/all.txt)       |
| 🔹 HTTP Only   | [http.txt](https://github.com/aesneverhere/proxyhub/blob/main/output/http.txt)     |
| 🔸 SOCKS4      | [socks4.txt](https://github.com/aesneverhere/proxyhub/blob/main/output/socks4.txt) |
| 🔸 SOCKS5      | [socks5.txt](https://github.com/aesneverhere/proxyhub/blob/main/output/socks5.txt) |

<p align="center">
  <a href="https://github.com/aesneverhere/proxyhub/blob/main/output/all.txt"><img src="https://img.shields.io/badge/📦 Semua-blue?style=for-the-badge"></a>
  <a href="https://github.com/aesneverhere/proxyhub/blob/main/output/http.txt"><img src="https://img.shields.io/badge/🔹 HTTP-orange?style=for-the-badge"></a>
  <a href="https://github.com/aesneverhere/proxyhub/blob/main/output/socks4.txt"><img src="https://img.shields.io/badge/🔸 SOCKS4-yellow?style=for-the-badge"></a>
  <a href="https://github.com/aesneverhere/proxyhub/blob/main/output/socks5.txt"><img src="https://img.shields.io/badge/🔸 SOCKS5-lightgrey?style=for-the-badge"></a>
</p>

---

## 📊 Statistik Realtime

<!-- PROXY_STATS_START -->
🔹 HTTP: 41205
🔸 SOCKS4: 2862
🔸 SOCKS5: 48
📦 Total: 44115
<!-- PROXY_STATS_END -->

---

## ⚙️ Jalankan Lokal

```bash
# Clone repo
$ git clone https://github.com/aesneverhere/ProxyHub && cd ProxyHub

# Install depedensi
$ pip install -r requirements.txt

# Jalankan semua siklus otomatis
$ python main.py

# Atau hanya API server
$ python flask_app.py
```

---

## 🔄 Auto Update

* Setiap 15 menit via `.github/workflows/deploy.yml`
* Output tersimpan di folder `output/`

---

## 🙌 Credits

* [proxifly/free-proxy-list](https://github.com/proxifly/free-proxy-list)
* [TheSpeedX/SOCKS-List](https://github.com/TheSpeedX/SOCKS-List)
* [officialputuid/KangProxy](https://github.com/officialputuid/KangProxy)
* [Zaeem20/FREE\_PROXIES\_LIST](https://github.com/Zaeem20/FREE_PROXIES_LIST)
* [roosterkid/openproxylist](https://github.com/roosterkid/openproxylist)

---

<p align="center">
  🐱 Built with ❤️ by <a href="https://github.com/aesneverhere">@aesneverhere</a>
</p>
