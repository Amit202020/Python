class  DicDemo:
	def   method1(self):
		dic   =  {    1 : "One" ,  2: "Two" , 2: "222" ,  3: "Three"}
		print(dic)
		
		dic1   =  {    
						1: "mobile" , 
					   "keytwo":  [456 , "ttt"] ,
					   (1,2,3): "cricket"
				  }
		print(dic1)
		
		#update
		dic1[1] = "laptop"
		print(dic1)
		
		#insert
		dic1[4] = "cup"
		print(dic1)
		
		#length
		print(len(dic1))
		
obj = DicDemo()
obj.method1()
			