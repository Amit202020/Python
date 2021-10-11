class    Product:
	pname ="electronics"
	
	def    __init__(self,pid,pname):
		self.prodId = pid
		self.prodName = pname
		
	def   method1(self):               # instance method
		print(str(self.prodId) +"/"+ self.prodName)
		
	@classmethod
	def  getProdDetails(cls):
		print("Product name is", cls.pname)
		
	@staticmethod
	def  method2():
		print("This is static method")
		
p  = Product(1005,"mobile")
p.method1()
p.getProdDetails()
p.method2()