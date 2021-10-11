class     FrozenDemo:
	def  method1(self):
		tp1  =  ('a','b','c','d','e')
		
		#tuple to frozenset
		fz1 = frozenset(tp1)
		print(fz1)
		
		ls1 = [9,7,45,32,76,9]
		#list to frozenset
		fz2  = frozenset(ls1)
		print(fz2)
		
		
obj = FrozenDemo()
obj.method1()