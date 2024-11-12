# index.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Establece el código de respuesta
        self.send_response(200)
        
        # Configura las cabeceras de la respuesta
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Escribe el contenido del mensaje
        message = "Hi, my name is Christian :3 am in python now!"
        self.wfile.write(message.encode("utf-8"))

# Configurar el puerto y el servidor
PORT = 8000
with HTTPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor iniciado en el puerto {PORT}")
    httpd.serve_forever()
