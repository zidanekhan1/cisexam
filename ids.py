from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class LoginHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <h2>IDS Practical Login</h2>
        <form method="POST">
            Username: <input name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <button>Login</button>
        </form>
        """)

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()
        form = parse_qs(data)

        username = form.get("username", [""])[0]
        password = form.get("password", [""])[0]

        if username == "student" and password == "Test123":
            result = "Login Successful"
        else:
            result = "Login Failed"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result.encode())


server = HTTPServer(("127.0.0.1", 8000), LoginHandler)

print("Server running at http://127.0.0.1:8000")
server.serve_forever()