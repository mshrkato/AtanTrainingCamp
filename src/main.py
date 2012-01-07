from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.hello import HelloWorld
from handlers.bye import ByeWorld
from handlers.yonta import Yonta

application = webapp.WSGIApplication([('/', HelloWorld),
                                      ('/bye/', ByeWorld),
                                      ('/yonta/',Yonta)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
