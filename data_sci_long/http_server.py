from  http.server import HTTPServer, BaseHTTPRequestHandler
from http.server import CGIHTTPRequestHandler
import sys, os

server_addr = ('localhost', 8000)
cgiServer = HTTPServer(server_addr, CGIHTTPRequestHandler)
sys.stderr.write('Localhost CGI server started\n.')
cgiServer.serve_forever()