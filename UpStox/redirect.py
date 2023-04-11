import http.server
import socketserver
import urllib.parse

PORT = 3000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        
        if "code" in query:
            code = query["code"][0]
            print(code)
            
            # Send the code value in the response body
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(code.encode("utf-8"))
        else:
            # If no code parameter is found, serve the file normally
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server started on port", PORT)
    httpd.serve_forever()
