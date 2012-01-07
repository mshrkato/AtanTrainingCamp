from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HelloWorld(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hello, World!")

application = webapp.WSGIApplication([('/', HelloWorld)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
