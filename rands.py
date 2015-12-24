#!/usr/bin/python
#Linux

from math import *
import timeit, time, random, sys, signal

print("Merry Christmas Dad! You get to do math to earn your gift.")
print("You'll see a random number pop up on the screen.")
print("Type its square correctly to move to the next problem.")
print("There are 7 problems...oh, and there's a time limit that decreases ")
print("with each problem :) The game will exit upon a wrong answer or timeout. ")
print("When you're ready, press enter to start!\n")

raw_input()

#make list of random numbers
mylist = []

for x in range(0, 6):
	rand = int(sqrt(random.randint(10,100)*random.randint(10,100)))
	while rand in mylist:
		rand = int(sqrt(random.randint(10,100)*random.randint(10,100)))
		if not rand in mylist:
			continue
	if not rand in mylist:
		mylist.append(rand)	
def addnum():
	lastNum = random.randrange(30, 100, 5)
	while lastNum in mylist:
		lastNum = random.randrange(30, 100, 5)
		if not lastNum in mylist:
			continue
	if not lastNum in mylist:
		mylist.append(lastNum)
addnum()

print mylist
#a,b,c,d,e,f,g = 0,1,2,3,4,5,6
#mylist = [a,b,c,d,e,f,g]
limits = [15,13,12,11,10,9,4]


#signal stuff
def interrupted(signum, frame):
	raise Exception("Sorry, you ran out of time!")
signal.signal(signal.SIGALRM, interrupted)

#guessing
def evaluateGuess(user_guess, variable):
	if user_guess == variable**2:
		print "Right!\n"
	else:
		if user_guess: #user_guess might also be Exception "exc" so you must skip it
			print "Sorry, that wasn't correct. Goodbye.\n"
		sys.exit()

#input
def rinput(TIMEOUT):
	signal.alarm(TIMEOUT)
	try:
		foo = input()
		signal.alarm(0)
		return foo
	except Exception, exc: 		# if input times out
		print exc
		return

for x in mylist:
	print "Square this number = ", x
	print "What's ur guess? You have {0} seconds".format(limits[mylist.index(x)])
	userguess = rinput(limits[mylist.index(x)])
	evaluateGuess(userguess, x)


print "Your gift is behind Jesus!"
