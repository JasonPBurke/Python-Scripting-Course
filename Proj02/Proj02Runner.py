import turtle

class Runner(object):

	print("Jason Burke")

	def __init__(self, tColor):#Initialize instance variables for this object using self
		self.color = tColor
		self.turtle = turtle.Turtle()
		self.name = "Jason Burke"

	def run(self):
		#set pensize and shape for object
		self.turtle.pensize(5)
		self.turtle.shape('turtle')

		turtleData = (self.color, self.turtle, self.name)
		return turtleData
