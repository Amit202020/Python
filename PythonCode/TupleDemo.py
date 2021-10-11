class    TupleDemo:
	def  method2(self):
	
		tp1 =  (5,6,7,8)
		print(tp1)
		
		#tuple to list
		tp2  =  list(tp1)
		print(tp2)
		
	    #list  to tuple
		tp3  = tuple(tp2)
		print(tp3)
		
		tp4  =  ('python','jython','mython')
		
		#concat
		print(tp3+tp4)
		
		#nesting
		tp5 = (tp3 ,tp3 , tp3)
		print(tp5)
		
		#repetation
		tp6  =  tp3 * 100
		print(tp6)
		
		
		print(tp3)
		tp3[0] = 77
		print(tp3)
	
	
	
			
obj = TupleDemo()
obj.method2()