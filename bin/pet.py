def pet(q):
	words = q.split(" ")
	animal = ""
	isPet = False
	for word in words :
		if isPet == True :
			animal = word.replace(".","")
			isPet = False
		if "pet" in word :
			isPet = True

	print "I want to meet your %s" % animal 
