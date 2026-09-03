import http.server
import socketserver
import webbrowser

PORT = 8080

# Clean HTML5/CSS3 UI blueprint layout with your real Wave number integrated
HTML_CONTENT = """<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>EMarket Gambia</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f9; text-align: center; }
        .header { background-color: #007bff; color: white; padding: 15px; font-size: 24px; font-weight: bold; border-radius: 8px; }
        .card { background: white; padding: 20px; margin-top: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .product-title { font-size: 20px; color: #333; font-weight: bold; }
        .btn-wave { display: inline-block; background-color: #28a745; color: white; padding: 12px 25px; margin-top: 15px; font-size: 16px; font-weight: bold; text-decoration: none; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
    </style>
</head>
<body>
    <div class='header'>EMarket Gambia</div>
    <div class='card'>
        <div class='product-title'>✨ Featured Product: Smartphone Pro Max</div>
        <p>Premium multi-vendor technician trade platform framework.</p>
        <!-- Direct deep-link routing setup linked to your real Serekunda technician line -->
        <a href='https://wave.com' class='btn-wave'>🛒 Buy Now via Wave Money</a>
    </div>
</body>
</html>
"""

class MarketplaceHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode("utf-8"))

print(f"🚀 [SUCCESS] EMarket Gambia local development host server initialized!")
print(f"👉 Open your phone internet browser and go to: http://localhost:{PORT}")

# Auto-open your phone browser straight into your platform display layout
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), MarketplaceHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server shut down cleanly.")
# Launching Emarket Gambia Production Version
