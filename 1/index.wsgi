import sae
from my import wsgi

application = sae.create_wsgi_app(wsgi.application)
