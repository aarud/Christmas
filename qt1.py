#!/usr/bin/python

import sys, timeit, random, signal
from PyQt4 import QtGui, QtCore
from math import *


'''
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(100,100,300,300)
window.setWindowTitle("my window")
window.show()
app.exec_()
'''

class Window1(QtGui.QMainWindow):
	def __init__(self):
		self.myinput = 'a'	
		QtCore.pyqtRemoveInputHook()
		super(Window1, self).__init__()
		self.setGeometry(500,100,700,300)
		self.setWindowTitle("my window")
		self.setWindowIcon(QtGui.QIcon('xpmas.png'))
		
		#add menu choice 
		newgame = QtGui.QAction("&New Game", self)
		newgame.setShortcut("Ctrl+N")
		newgame.setStatusTip('Start a new game')
		newgame.triggered.connect(self.game)
				
		self.statusBar()
		
		#add menu and menu items
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(newgame)
		
		#add buttons, box
		self.lbl = QtGui.QLabel(self, text = 'Your Guess: ')
		self.lbl.move(50,50)
		self.box = QtGui.QLineEdit(self)
		self.box.move(50,80)
		self.box.setPlaceholderText('Enter your guess')
		self.box.resize(self.box.sizeHint())
		self.box.textChanged.connect(self.getText)

		self.okbtn = QtGui.QPushButton("OK", self)
		self.okbtn.clicked.connect(self.getText)
		self.okbtn.resize(self.okbtn.sizeHint())
		self.okbtn.setAutoDefault(True)
		self.okbtn.move(50,110)
		
		inputlabel = QtGui.QLabel(self, text = 'Inputted: ')
		inputlabel.move(50,160)
		self.inputted = QtGui.QLineEdit(self)
		self.inputted.resize(self.box.sizeHint())
		self.inputted.move(50,190)

		self.qbtn = QtGui.QPushButton("Quit", self)
		self.qbtn.clicked.connect(self.close_app)
		self.qbtn.resize(self.qbtn.sizeHint())
		self.qbtn.move(50,220)

		self.box.returnPressed.connect(self.qbtn.click)

		#add toolbar choice
		self.newgame = QtGui.QAction(QtGui.QIcon('xpmas'), 'New game', self)
		self.newgame.triggered.connect(self.game)
		
		#add toolbar
		self.toolbar = self.addToolBar("New Game")
		self.toolbar.addAction(self.newgame)
		
		self.show()
	
	def getText(self):
		self.myinput = self.box.text()
		if self.myinput == 'a':
			print self.myinput
		self.inputted.setText(self.myinput)

	def close_app(self):
		print("Goodbye")
		sys.exit()
	
	def sayHi(self, arg):
		print "hello"
	
	def game(self):
		print("Merry Christmas Dad! You get to do math to earn your gift.")
		print("You'll see a random number pop up on the screen.")
		print("Type its square correctly to move to the next problem.")
		print("There are 7 problems...oh, and there's a time limit that decreases ")
		print("with each problem :) The game will exit upon a wrong answer or timeout. ")
		print("When you're ready, press enter to start!\n")

		raw_input()

		#make list of random numbers
		mylist = []
		'''
		def makeList():
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
		makeList()
		addnum()
		'''

		a,b,c,d,e,f,g = 0,1,2,3,4,5,6
		mylist = [a,b,c,d,e,f,g]
		limits = [15,13,12,11,10,9,4]


		#signal stuff
		def interrupted(signum, frame):
			raise Exception("Sorry, you ran out of time!")
		signal.signal(signal.SIGALRM, interrupted)

		#guessing
		def guess(user_guess, variable):
			if user_guess == variable**2:
				#show on screen: "Right!\n"
				print "Right!\n"
				#make new QLineEdit
			else:
				#show on screen: "Sorry..."
				if user_guess:
					print "Sorry, that wasn't correct. Goodbye.\n"
				#reset window? Just stop the game...not the application
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
				
		def doGame():
			for x in mylist:			
				print "Square this number = ", x
				print "What's ur guess? You have {0} seconds".format(limits[mylist.index(x)])
				userguess = rinput(limits[mylist.index(x)])
				guess(userguess, x)
		doGame()
		
		print "Ur gift iz behind Jesus"
		sys.exit()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window1()
	sys.exit(app.exec_())
	
run()

