class FizzBuzzer():
	def __init__(self):
		self.count = 0

	def call(self):
		self.count = self.count + 1
		if self.count % 3 == 0:
			reply = 'fizz';
		else:
			reply = str(self.count);
		return reply
