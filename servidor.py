from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit, parse_qs


def _pagina(texto):
    return f"<html><body><h1>{texto}</h1></body></html>"


def responder(ruta):
    """Devuelve (status, cuerpo_html) para una ruta con query string."""
    partes = urlsplit(ruta)
    if partes.path == "/":
        return 200, _pagina("Hola mundo")
    if partes.path == "/saludo":
        nombre = parse_qs(partes.query).get("nombre", ["desconocido"])[0]
        return 200, _pagina("Hola, " + escape(nombre))
    return 404, _pagina("No encontrado")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, cuerpo = responder(self.path)
        datos = cuerpo.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)


if __name__ == "__main__":
    HTTPServer(("", 8000), Handler).serve_forever()
