from google.appengine.ext import webapp

class ByeWorld(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Bye, World!!")
        self.response.out.write('''
            <form method="post" action="/bye/">
                <textarea name="text"></textarea>
                <input type="submit"></input>
            </form>
        ''')
    def post(self):
        text = self.request.get("text")
        self.response.out.write(text)