class   Pen:

	def __init__(self,clrr,cst):
		self.color = clrr
		self.cost  = cst
		print("This is para constructor")
		
	def __init__(self):
		print("This is deafult constructor")
		
			
	def   write(self):
		print("The color is "+self.color)
		print("The cost is "+ str(self.cost))
			
##calling papa const
##pobj1 = Pen('red',100.00)

##calling default const
pobj1 = Pen()    

##pobj1.write()