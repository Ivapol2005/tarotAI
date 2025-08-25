import http.server
import ssl

PORT = 8000

# Створюємо сервер
server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Обгортаємо сокет SSL
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="key.pem",
                               certfile="cert.pem",
                               server_side=True)

print(f"Serving HTTPS on https://localhost:{PORT}")
httpd.serve_forever()
