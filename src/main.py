from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.hello import HelloWorld
from handlers.yonta import Yonta
from handlers.gege import  Gegegege 

application = webapp.WSGIApplication([('/yonta/',Yonta),
                                      ('/', HelloWorld),
                                      ('/naga/',Gegegege )],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
