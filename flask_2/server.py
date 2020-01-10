from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print('server http on the 8000....')
httpd.serve_forever()