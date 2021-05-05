# Library WSGI
from wsgiref.simple_server import make_server

# HTML
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1> Hola clase de python, código</h1>
</body>
</html>
"""


def application(environ, start_response):
  header = [('Content-type','text/html; charset=utf-8')]

  # Response code
  start_response('200 OK', header)

  return [bytes(HTML,'utf-8')]

server = make_server('localhost',8000, application)
print("Start server on port 8000.....")
server.serve_forever()