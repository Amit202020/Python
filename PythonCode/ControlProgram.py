class	ControlProgram:
	def method2(self):
		x = 7
		y = 6
		if  x > y:
			print("x is larger than y")
		elif x == y:
			print("x equals to y")
		elif x < y:
			print("x is smaller than y")
		else:
			print("nothing is true")
			
			
		s1 =  "World"
		s2 = "Good Bye World"
		if   "World" in  s1:
			print("string contain the word world")
		elif  "World"  not in  s1:
			print("string does not contain the word world")
			
obj =  ControlProgram()
obj.method2()