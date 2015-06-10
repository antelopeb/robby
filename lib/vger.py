class Vger :
	# initialize Vger
	def _init(self) :
		print "Intializing Vger"
		print "I am Vger. What can I do for you?"

	# ask function to process questions
	def ask(self, q) :
		if q == "quit":
			print "quitting"
		elif q == "how are you?":
			print "I am fine, thank you."
			self.askNew()
		else:
			print "I don't understand your command, %s" % q
			self.askNew()

	# ask a new question
	def askNew(self) :
		qnew = raw_input(prompt)
		self.ask(qnew)


vger = Vger()
prompt = ">>"

# run the init on Vger
vger._init()
# ask the first question to start the looping
q = raw_input(prompt)
vger.ask(q)

