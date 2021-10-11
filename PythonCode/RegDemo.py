import moduleone

class  RegDemo:
	def  __init__(self):
		try:
			age =input("Enter your age")
			g = int(age)
			if g < 20 :
				raise moduleone.AgeOutOfRangeException("The input age is out of range")
			else:
				print("Thanks for your input")
		except  Exception as  e:
			print(e)
		
obj =  RegDemo()