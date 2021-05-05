# Library WSGI
from wsgiref.simple_server import make_server

def application(environ, start_response):
  header = [('Content-type','text/plain; charset=utf-8')]

  # Response code
  start_response('200 OK', header)

  return ['Hola primer servidor web en python a patita =)'.encode('utf-8')]

server = make_server('localhost',8000, application)
server.serve_forever()