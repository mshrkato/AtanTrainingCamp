from google.appengine.ext import webapp

class Gegegege(webapp.RequestHandler):
    def get(self):
        self.response.out.write("o, World!!")
