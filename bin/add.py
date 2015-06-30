phrase = ["add", "sum"]

def main(q, prompt):
    qs = q.split(" ")
    numbers = []
    
    for word in qs :
        word = word.replace(',', "")
        try :
            num = float(word)
            numbers.append(num)
        except :
            pass
        
    added = 0
    
    for num in numbers :
        added = added + num
    
    print "Your answer is: %r" % added
