mport json
import csv

with open("output/geo/geo_http.json") as f:
    data = json.load(f)

with open("output/geo/geo_http.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ip", "type", "country", "isp", "latency_ms", "proxy"])
    writer.writeheader()
    writer.writerows(data)

print("✅ CSV disimpan ke output/geo/geo_http.csv")
