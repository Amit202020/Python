class	EmpDetails:
	def   inputDetails(self):
		self.empId = input("please enter empid ")
		self.empName = input("please enter emp name ")
		self.empEmail = input("please enter emp email")
		
	def   printDetails(self):
		print(type(self.empId))
		print("The emp id is "+ self.empId)
		print("The empname is "+ self.empName)
		print("The emp email is "+  self.empEmail)
		
obj =  EmpDetails()  
obj.inputDetails()
obj.printDetails()