from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ProxyHub API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #333;
            }
            a {
                color: #007BFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .box {
                background: white;
                padding: 20px;
                margin: auto;
                display: inline-block;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🌐 ProxyHub API</h1>
            <p>Welcome! Here are the available endpoints:</p>
            <ul style="text-align: left;">
                <li><a href="/http">/http</a> – List HTTP proxies</li>
                <li><a href="/socks4">/socks4</a> – List SOCKS4 proxies</li>
                <li><a href="/socks5">/socks5</a> – List SOCKS5 proxies</li>
                <li><a href="/geo">/geo</a> – GeoIP proxy list</li>
                <li><a href="/update">/update</a> – Manually trigger update</li>
            </ul>
            <p>👤 <a href="https://github.com/aesneverhere" target="_blank">@aesneverhere</a></p>
        </div>
    </body>
    </html>
    """)
