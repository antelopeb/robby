import os

class Vger :
    # define the new array
    bindings = {}
    names = []
    # initialize Vger
    def _init(self) :
        print "Intializing Vger"
        
        # bring in dependencies, and assign their names
        # to an array on Vger of the defined functions
        print "Loading the following modules"
        files = os.listdir("./bin")
        for file in files:
            if ("__init__" not in file) and (".pyc" not in file) :
                file = file.replace(".py", "")
                print file
                self.bindings[file] = (__import__('bin.'+file, fromlist=["bin"]))
                self.names.append(file)        
        
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
        
        for name in self.names :
            if (name in q) :
                isCommand = True
                command = name
        
        if (q == "quit") or (q == "q") :
            print "quitting"
        elif ("how are you" in q) or ("how ya doing" in q) or ("how's it hanging" in q) :
            # a simple response to a how are you
            print "I am a computer, and have no feelings. Please enter a command instead of making small talk."
            askNew()
	elif ("small talk" in q) :
		print "It was too small talk. I'm shutting down now."
        elif (isCommand == True) :
            getattr(self.bindings[command], command)(q)
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

