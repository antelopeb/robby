import os

class Vger :
    # define the new array
    bindings = {}
    phrases = []
    files = []
    # initialize Vger
    def _init(self) :
        print "Intializing Vger"
        
        # bring in dependencies, and assign their names
        # to an array on Vger of the defined functions
        print "Loading modules"
        files = os.listdir("./bin")
        for file in files:
            if ("__init__" not in file) and (".pyc" not in file) and (".DS_Store" not in file) :
                file = file.replace(".py", "")
                print file
                self.bindings[file] = (__import__('bin.'+file, fromlist=["bin"]))
                for phrase in self.bindings[file].phrase :                    
                    self.phrases.append(phrase)
                    self.files.append(file)
        
        print "I am Vger. What can I do for you?"

    # ask function to process questions
    def ask(self, q) :
        # ask a new question
        def askNew() :
            qnew = raw_input(prompt)
            self.ask(qnew)

        # lowercase the question for better comparisons
        q = q.lower()
        
        # find out if the command is available
        isCommand = False
        
        i = 0
        for phrase in self.phrases :
            if (phrase in q) :
                isCommand = True
                command = self.files[i]
            i = i+1
        
        if (q == "quit") or (q == "q") :
            print "quitting"
        elif (isCommand == True) :
            getattr(self.bindings[command], 'main')(q, prompt)
            askNew()
        else :
            print "I don't understand your command, %s" % q
            askNew()


vger = Vger()
prompt = ">>"

# run the init on Vger
vger._init()
# ask the first question to start the looping
q = raw_input(prompt)
vger.ask(q)

