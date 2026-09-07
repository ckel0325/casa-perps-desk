#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
if __name__ == "__main__":
    print("Casa Perps HUD  http://127.0.0.1:8765/casa-perps-hud.html")
    ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()
