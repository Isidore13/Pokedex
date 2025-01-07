#coding:utf-8
import http.server
import sqlite3

conn = sqlite3.connect('pokedex.db')
cur = conn.cursor()
conn.commit()

port = 80
address = ("",port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address,handler)

print(f"Serveur démarré sur le PORT {port}")
httpd.serve_forever()