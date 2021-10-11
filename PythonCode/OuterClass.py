class    OuterClass:
	message = "This is outer class class var"
	def  __init__(self):
		self.obj = self.InnerClass()
		
	class  InnerClass:
		def  printMessage(self):
			return   OuterClass.message
			
outerinstance = OuterClass()
print(outerinstance.obj.printMessage())