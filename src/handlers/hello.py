from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.greeting import Greeting

from os.path import dirname, join

class HelloWorld(webapp.RequestHandler):
    def get(self):
        greetings = Greeting.all()

        values = {'greetings' : greetings}
        path = join(dirname(dirname(__file__)), 'template', 'hello.html')
        body = template.render(path, values)
        body = 'Hello world!'
        self.response.out.write(body)

    def post(self):
        name = self.request.get('name')
        age = int(self.request.get('age'))
        content = self.request.get('content')

        greeting = Greeting(name=name,age=age,content=content)

        greeting.put()

        self.redirect('/')
