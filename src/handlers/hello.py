from google.appengine.ext import webapp

class HelloWorld(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hello, World!!")
