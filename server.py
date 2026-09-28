import http.server
import socketserver
import platform

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            specs = f"""
            <html>
            <head>
                <title>Laptop Device Specifications</title>
            </head>
            <body>
                <h1>Laptop Device Specifications</h1>

                <p><b>Name:</b> KIMTHY CHARLES</p>
                <p><b>Register Number:</b> 26013433</p>
                <p><b>Operating System:</b> {platform.system()}</p>
                <p><b>OS Version:</b> {platform.version()}</p>
                <p><b>Machine:</b> {platform.machine()}</p>
                <p><b>Processor:</b> {platform.processor()}</p>

            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(specs.encode())

        else:
            self.send_error(404)

with socketserver.TCPServer(("", PORT), MyHandler) as server:
    print(f"Server started at http://127.0.0.1:{PORT}")
    server.serve_forever()