class   ExceptionDemo:
	def method1(self):
	    
		a = 10
		b = 0
	try:
		print('inside try block')
		c = a/b
		print(c)
	except  Exception:
		print("Exception Cought")
		
	finally:
		print("This is finally block")
		
obj = ExceptionDemo()
obj.method1()