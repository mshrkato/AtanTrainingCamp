from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.hello import HelloWorld
from handlers.bye import ByeWorld

application = webapp.WSGIApplication([('/', HelloWorld),
                                      ('/bye', ByeWorld)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
