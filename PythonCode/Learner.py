class   Learner:
	def   setName(self,name):
		self.name = name
		
	def  getName(self):
		return self.name
		
obj =  Learner()
obj.setName("Max")
print(obj.getName())
