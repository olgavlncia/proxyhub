<p align="center">
  <img src="https://github.com/images/mona-whisper.gif" width="120" alt="ProxyHub Cat Logo" />
</p>

<h1 align="center">🛰️ ProxyHub</h1>

<p align="center">
  🔌 Free Proxy Scraper · 🌍 Geo Lookup · 📄 JSON & CSV Export · ✨ Auto Update via GitHub Actions
</p>

<p align="center">
  <img alt="Last Update" src="https://github.com/aesneverhere/ProxyHub/actions/workflows/deploy.yml/badge.svg">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square">
  <img alt="License" src="https://img.shields.io/github/license/aesneverhere/ProxyHub?style=flat-square">
</p>

---

## 🚀 Fitur Utama

* ✅ Scrape proxy HTTP / SOCKS4 / SOCKS5 dari banyak sumber
* 🔍 Filter proxy aktif secara async (super cepat)
* 🌍 GeoIP lookup & latency test
* 📄 Export ke `.json` dan `.csv`
* ✨ Auto update tiap 15 menit (via GitHub Actions)
* 🌐 Public API siap pakai (Flask + Railway)

---

## 🌐 API Publik

> Base URL: `https://proxyhub.up.railway.app`

| Endpoint  | Keterangan                       |
| --------- | -------------------------------- |
| `/`       | Welcome JSON                     |
| `/http`   | List proxy aktif HTTP            |
| `/socks4` | List proxy aktif SOCKS4          |
| `/socks5` | List proxy aktif SOCKS5          |
| `/geo`    | JSON proxy aktif + geo + latency |

```

---

## 📊 Dashboard Realtime

<!-- PROXY_STATS_START -->
(akan diupdate otomatis)
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

# Atau jalankan hanya API server
$ python flask_app.py
```

---

## 🔄 Auto Update via GitHub Actions

Proxy aktif diperbarui otomatis:

* ⏱️ Setiap 15 menit (`.github/workflows/deploy.yml`)
* Hasil tersimpan di folder `output/`

---

## 👥 Credits

* [proxifly/free-proxy-list](https://github.com/proxifly/free-proxy-list)
* [TheSpeedX/SOCKS-List](https://github.com/TheSpeedX/SOCKS-List)
* [officialputuid/KangProxy](https://github.com/officialputuid/KangProxy)
* [Zaeem20/FREE\_PROXIES\_LIST](https://github.com/Zaeem20/FREE_PROXIES_LIST)
* [roosterkid/openproxylist](https://github.com/roosterkid/openproxylist)

---

<p align="center">
  🐱 Powered by <strong>ProxyHub</strong> — crafted with love by <a href="https://github.com/aesneverhere">@aesneverhere</a>
</p>
