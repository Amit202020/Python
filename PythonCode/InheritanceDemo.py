class    Shape:
	def   area(self):
		print("This is shape class")
		
class   Circle(Shape):
	def   circlearea(self):
		print("This is area of circle")
		
obj1 = Circle()
obj1.area()
obj1.circlearea()