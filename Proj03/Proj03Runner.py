import turtle

class Runner(object):

	print("Jason Burke")

	def __init__(self, tColor):
		Runner.color = tColor# set the incomming color to a new class variable color
		Runner.name = "Jason Burke"# set class variable name
		self.turtle = turtle.Turtle()# set instance variable turtle

	def run(self):

		self.turtle.pensize(5)
		self.turtle.shape("turtle")

		tData = (self.color, self.turtle, self.name)

		return tData