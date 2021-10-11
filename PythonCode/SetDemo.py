class  SetDemo:
	def   method1(self):
	
		# list   ------------->   set
		ls1  =     [22,44,55]
		st1  =     set(ls1)
		print(st1)
		
		#tuple  --->  set		
		tp1  =  (7,8,3)
		st2  = set(tp1)
		print(st2)
		
		st3  =  {11, 12, 11, 14 ,17}
		
		st4  =  {70 , 80 , 11  ,  14  , 55}
		
		st5 =   st3.difference(st4) 
		print(st4)
		
		
obj = SetDemo()
obj.method1()
			