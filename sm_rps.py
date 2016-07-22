from random import choice
compscore = 0
userscore = 0

print "Hi, I'm Sydney the computer. Let's play a game of rock-paper-scissors!"
def sydney(move, compscore, userscore):	
	x = choice("rps")
	if move == "r" and x == "r":
		print "I play rock."
		print "We tied!"
		return compscore, userscore
	elif move == "r" and x == "s":
		print "I play scissors."
		print "You win!"
		return compscore, userscore + 1
	elif move == "r" and x == "p":
		print "I play paper."
		print "I win!"
		return compscore + 1, userscore
	if move == "p" and x == "p":
		print "I play paper."
		print "We tied!"
		return compscore, userscore
	elif move == "p" and x == "s":
		print "I play scissors."
		print "I win!"
		return compscore + 1, userscore
	elif move == "p" and x == "r":
		print "I play rock."
		print "You win!"
		return compscore, userscore + 1
	if move == "s" and x == "s":
		print "I play scissors."
		print "We tied!"
		return compscore, userscore
	elif move == "s" and x == "p":
		print "I play paper."
		print "You win!"
		return compscore, userscore + 1
	elif move == "s" and x == "r":
		print "I play rock."
		print "I win!"
		return compscore + 1, userscore


x = 0
y = 0

move = raw_input("Make your move (r, p, s) or 'quit' to quit: ")
while move != "quit":
	x, y = sydney(move, x, y)
	print x, y

	move = raw_input("Make your move (r, p, s) or 'quit' to quit: ")

print "Game over. Final score: Me: %d, You: %d" % (x, y)