from google.appengine.ext import webapp

class HelloWorld(webapp.RequestHandler):
    def get(self):
        user = self.request.get('user')
        age = self.request.get('age')
        self.response.out.write("%s is %s years old." % (user, age))
