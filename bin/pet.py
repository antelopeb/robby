phrase = ["i have a pet"]

def main(q,p):
    # split the question up into an array
	words = q.split(" ")
	animal = ""
	isPet = False
    # loop through the array and look for the word "pet"
    # assume the next word is the persons pet
	for word in words :
		if isPet == True :
			animal = word.replace(".","")
			isPet = False
		if "pet" in word :
			isPet = True

	print "I want to meet your %s" % animal 
