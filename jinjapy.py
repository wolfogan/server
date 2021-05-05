from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server

# Library WSGI




def application(environ, start_response):

  # Load folder and template html
  env = Environment(loader=FileSystemLoader("templates"))


  template = env.get_template('template.html')

  # Generate data
  data = {
    'title': 'WSGI template render with Jinja',
    'username': 'Tatakae, Tatakae, dudmit'
  }

  # Render template
  html = template.render(data)

  headers = [('Content-type','text/html; charset=utf-8')]

  # Response code
  start_response('200 OK', headers)

  return [bytes(html,'utf-8')]

# Release reources
with make_server('localhost',8000, application) as httpd:
  print("Start server on port 8000.....")
  httpd.serve_forever()