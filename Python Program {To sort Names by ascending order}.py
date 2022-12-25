def sortSur(nameList):
	l2 = []

	for ele in nameList:
		l2.append(ele.split())
	nameList = []

	for ele in sorted(l2, key=lambda x: x[-1]):
		nameList.append(' '.join(ele))
	return nameList
nameList = input("Enter names: ").split()
print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))
