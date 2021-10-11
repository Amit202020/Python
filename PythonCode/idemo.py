class   AA:

    #variable
	#method
	def   __init__(self,a,b):
		self.x = a
		self.y = b
		print(self.x ,"/",self.y)

class   BB(AA):
	def  __init__(self,a,b,c):
		super().__init__(a,b)
		self.z = c
		print(self.x ,"/",self.y , "/",self.z)
		
		
	
obj = BB(20,30,40)