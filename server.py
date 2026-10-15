import http.server
import socketserver
import os

PORT = 8085
os.chdir(r"C:\Users\lenovo\Documents\Daily_AI_Tools\mantarjantar_official")

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        ctype = super().guess_type(path)
        if ctype.startswith('text/') or ctype.endswith('javascript'):
            return ctype + '; charset=utf-8'
        return ctype

with socketserver.TCPServer(("", PORT), UTF8Handler) as httpd:
    print(f"Serving at http://localhost:{PORT} with forced UTF-8")
    httpd.serve_forever()
