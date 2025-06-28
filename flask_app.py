from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "message": "Welcome to ProxyHub API!",
        "endpoints": ["/http", "/socks4", "/socks5", "/geo"]
    }

@app.route("/http")
def http():
    with open("output/active/http.txt") as f:
        return jsonify(f.read().splitlines())

@app.route("/socks4")
def socks4():
    with open("output/active/socks4.txt") as f:
        return jsonify(f.read().splitlines())

@app.route("/socks5")
def socks5():
    with open("output/active/socks5.txt") as f:
        return jsonify(f.read().splitlines())

@app.route("/geo")
def geo():
    with open("output/geo/geo_http.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
