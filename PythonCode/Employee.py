class   Employee:

	aa  =  10     # static var
	
	def   __init__(self,eid,ename):
		self.empId=eid  ## instance var
		self.empName=ename
		
	def   printDemo(self):
		print(Employee.aa)
		
	def   display(self):
		c  = 20    ## local var
		print("The value is "+ str(c))
		
	def   method1(self):
		Employee.aa = Employee.aa +1
		
obj = Employee(1001,"max")
#print(obj.empId)
#print(obj.empName)
#obj.display()
obj.printDemo()   # 10
obj.method1()   # 11
obj.printDemo()  # 11


obj1 = Employee(1002,"max")
obj1.printDemo()
obj1.method1()
obj1.printDemo()













