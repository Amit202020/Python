class  AA:
	def	m1(self):
		print("inside aa class")
		
class	BB:
	def	m1(self):
		print("inside bb class")
		
class   CC(BB,AA):
	def  m3(self):
		print("Inside CC class")
		
obj  =   CC()
obj.m1()
