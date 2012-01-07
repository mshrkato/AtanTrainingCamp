from google.appengine.ext import webapp

class ByeWorld(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Bye, World!!")
