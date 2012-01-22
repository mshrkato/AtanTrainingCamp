from google.appengine.ext import db

class Greeting(db.Model):
    name = db.StringProperty()
    age = db.IntegerProperty()
    content = db.StringProperty()
