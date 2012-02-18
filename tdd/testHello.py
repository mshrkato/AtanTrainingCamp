from webtest import TestApp
from main import application
from nose.tools import *

app = TestApp(application())

def test_index():
  response = app.get('/')
  #ok_(True)
  assert 'Hello world!' in str(response)
