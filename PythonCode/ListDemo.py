class    ListDemo:
	def   method1(self):
		plist = []
		plist.append(111)
		plist.append(222)
		plist.append(333)
		plist.append(79)
		plist.append(800)
		plist.append(40)
		print(plist)
		print(plist[0])   # get the element
		plist[2]=888     #update element
		print(plist)
		print(len(plist))
		plist.sort()     # sort ascending order
		print(plist)
		plist.sort(reverse=True)     # sort decending order
		print(plist)
		plist.insert(4,"999")
		print(plist)
		plist.insert(5,"997")
		print(plist)
		plist.insert(3,"764")
		print(plist)
		plist.remove("764")
		print(plist)
		plist.remove("999")
		print(plist)
		
		plist1 = [40,50,60]
		plist.append(plist1)  # add sublist in the list
		print(plist)
		
		plist2 = [8,9,7]
		plist.extend(plist2)   # add more object in the same list
		print(plist)
		
		del  plist[1]
		print(plist)
		
		plist.remove(plist1)
		print(plist)
		
		
obj = ListDemo()
obj.method1()