from fizzbuzz import FizzBuzzer
from nose.tools import *

class TestFizzBuzz():
	def testFirstCall(self):
		"1st call"
		fizzbuzzer = FizzBuzzer()
		eq_('1', fizzbuzzer.call())

	def testSecondCall(self):
		"2nd call"
		fizzbuzzer = FizzBuzzer()
		fizzbuzzer.call()
		eq_('2', fizzbuzzer.call())

	def testThirdCall(self):
		"3rd call"
		fizzbuzzer = FizzBuzzer()
		fizzbuzzer.call()
		fizzbuzzer.call()
		eq_('fizz', fizzbuzzer.call())
