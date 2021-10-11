class    MultiDemo:
	def  method2(self):
		a  = [
			[4,5,6],
			[20,30,40],
			[60,30,10]
			]
		print(a)
		for i in range(len(a)):
			for j in range(len(a[i])):
				print(a[i][j])
			
obj = MultiDemo()
obj.method2()