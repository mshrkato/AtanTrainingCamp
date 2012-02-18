from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from os.path import dirname, join

class HelloWorld(webapp.RequestHandler):
    def get(self):
        user = self.request.get('user')
        age = self.request.get('age')

        values = {'user' : user, 'age' : age}
        path = join(dirname(dirname(__file__)), 'template', 'hello.html')
        body = template.render(path, values)
        body = 'Hello world!'
        self.response.out.write(body)
