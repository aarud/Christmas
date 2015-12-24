# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Squares.ui'
#
# Created: Tue Dec 22 15:24:43 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from math import *
import timeit, time, random, sys, signal


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    #global mylist
    #mylist = [0,1,2,3,4,5,6]
    global limits 
    limits = [15,13,12,11,10,9,4]

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        QtCore.pyqtRemoveInputHook()
        self.setupUi(self)

    def makelist(self):
        for x in range(0, 6):
            rand = int(sqrt(random.randint(10,100)*random.randint(10,100)))
            while rand in self.mylist:
                rand = int(sqrt(random.randint(10,100)*random.randint(10,100)))
                if not rand in self.mylist:
                    continue
            if not rand in self.mylist:
                self.mylist.append(rand) 
    def addnum(self):
        lastNum = random.randrange(30, 100, 5)
        while lastNum in self.mylist:
            lastNum = random.randrange(30, 100, 5)
            if not lastNum in self.mylist:
                continue
        if not lastNum in self.mylist:
            self.mylist.append(lastNum)

    def setupUi(self, MainWindow):
        self.movie = QtGui.QMovie('giphy2.gif')
        self.mylist = []
        self.makelist()
        self.addnum()
        self.userguess = 0
        self.qt_x = 0
        self.counter = 0
        self.myTimer = QtCore.QTimer()
        self.myTimer.timeout.connect(self.qt_endGame)
        self.winmsg = QtGui.QMessageBox()
        self.winmsg.setText('Your gift is hidden behind baby Jesus!')
        self.winmsg.setWindowTitle('You win!!!')

        #main window and Stacked Widget
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(335, 330)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))

        #PAGE 1
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.txt_instructions = QtGui.QTextBrowser(self.page)
        self.txt_instructions.setGeometry(QtCore.QRect(10, 21, 300, 239))
        self.txt_instructions.setObjectName(_fromUtf8("txt_instructions"))
        self.nextButton = QtGui.QPushButton(self.page)
        self.nextButton.setGeometry(QtCore.QRect(10, 260, 98, 27))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.stackedWidget.addWidget(self.page)

        #PAGE 2
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.startButton = QtGui.QPushButton(self.page_2)
        self.startButton.setGeometry(QtCore.QRect(10, 190, 98, 27))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.text_p2 = QtGui.QTextBrowser(self.page_2)
        self.text_p2.setGeometry(QtCore.QRect(10, 30, 256, 51))
        self.text_p2.setObjectName(_fromUtf8("text_p2"))
        self.stackedWidget.addWidget(self.page_2)

        #PAGE 3
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        #guess box
        self.guessBox = QtGui.QLineEdit(self.page_3)
        self.guessBox.setGeometry(QtCore.QRect(20, 100, 131, 27))
        self.guessBox.setObjectName(_fromUtf8("guessBox"))
        self.lbl_num = QtGui.QLabel(self.page_3)
        self.lbl_num.setGeometry(QtCore.QRect(20, 20, 250, 27))
        self.lbl_num.setObjectName(_fromUtf8("lbl_num"))
        #button for checking guess
        self.lbl_guess = QtGui.QLabel(self.page_3)
        self.lbl_guess.setGeometry(QtCore.QRect(20, 80, 111, 17))
        self.lbl_guess.setObjectName(_fromUtf8("lbl_guess"))
        self.btn_check = QtGui.QPushButton(self.page_3)
        self.btn_check.setGeometry(QtCore.QRect(20, 130, 98, 27))
        self.btn_check.setObjectName(_fromUtf8("btn_check"))
        self.stackedWidget.addWidget(self.page_3)

        #PAGE 4
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.txt_win = QtGui.QTextBrowser(self.page_4)
        self.txt_win.setObjectName(_fromUtf8("txt_win")) 
        self.movie_screen = QtGui.QLabel(self.page_4)
        self.movie_screen.setGeometry(QtCore.QRect(20, 80, 111, 17))
        self.verticalLayout_2.addWidget(self.txt_win)
        self.verticalLayout_2.addWidget(self.movie_screen)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.stackedWidget.addWidget(self.page_4)

        #menu bar and Stacked Widget
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtGui.QAction(MainWindow)
        self.actionNew_Game.setObjectName(_fromUtf8("actionNew_Game"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionNew_Game)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def display0(self):
        self.stackedWidget.setCurrentIndex(0)
    def display1(self):
        self.stackedWidget.setCurrentIndex(1)   
    def display2(self):
        self.stackedWidget.setCurrentIndex(2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Squares", None))
        self.txt_instructions.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0000ff;\">M</span><span style=\" font-weight:600; color:#00aaff;\">er</span><span style=\" font-weight:600; color:#0000ff;\">r</span><span style=\" font-weight:600; color:#00aaff;\">y</span><span style=\" color:#00aaff;\"> </span><span style=\" font-weight:600; color:#e20707;\">Ch</span><span style=\" font-weight:600; color:#00aa00;\">ri</span><span style=\" font-weight:600; color:#e20707;\">st</span><span style=\" font-weight:600; color:#00aa00;\">m</span><span style=\" font-weight:600; color:#e20707;\">as</span> Dad! You get to do math to earn your gift!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To find out where your gift is hidden, you have to beat this game.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You will have to solve several squares in a row correctly to get the answer.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oh...and there\'s a decreasing time limit for each question.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The game exits if you run out of time or type the wrong answer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Good luck!</p></body></html>", None))
        self.startButton.setText(_translate("MainWindow", "Start!", None))
        self.text_p2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When you\'re ready to start the game, just press start!</p></body></html>", None))
        self.txt_win.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">YOU </span><span style=\" font-size:36pt; font-weight:600; color:#ff0000;\">W</span><span style=\" font-size:36pt; font-weight:600; color:#00aa00;\">I</span><span style=\" font-size:36pt; font-weight:600; color:#ff0000;\">N</span><span style=\" font-size:36pt; font-weight:600; color:#00aa00;\">!</span><span style=\" font-size:36pt; font-weight:600; color:#ff0000;\">!</span><span style=\" font-size:36pt; font-weight:600; color:#00aa00;\">!</span></p></body></html>", None))
        self.lbl_num.setText(_translate("MainWindow", "Number: ", None))
        self.lbl_guess.setText(_translate("MainWindow", "Your guess:", None))
        self.btn_check.setText(_translate("MainWindow", "Check me!", None))
        self.nextButton.setText(_translate("MainWindow", "Next!", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game", None))
        self.actionNew_Game.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Esc", None))

        self.nextButton.clicked.connect(self.display1) #p0 to p1
        self.startButton.clicked.connect(self.qt_startGame) #p1 to p2(game)
        
        self.btn_check.clicked.connect(self.on_btn_click) #check game
        self.guessBox.returnPressed.connect(self.btn_check.click)
    
    def popNum(self, x):
        self.qt_x = x
        self.lbl_num.setText("Square this: {0}.\nYou have {1} seconds".format(x, limits[self.mylist.index(x)]))
    
    def on_btn_click(self):
        self.myTimer.stop()
        self.userguess = self.guessBox.text()
        self.qt_evaluateGuess(self.userguess, self.qt_x)
        return self.userguess    #may not need this line...

    def qt_evaluateGuess(self, user_guess, variable):
        try:
            user_guess = int(user_guess)
        except Exception:
            print "guess is NaN"
            pass
        try:
            variable = int(variable)
        except Exception:
            print "variable is NaN"
            pass

        if user_guess == variable**2:
            if self.counter < (len(self.mylist)-1):
                self.guessBox.clear()
                self.counter += 1
                self.qt_x = self.mylist[self.counter]
                self.qt_doGame(self.qt_x)
            else:
                self.youWin()
        else:
            if user_guess:
                self.wrongmsg = QtGui.QMessageBox.warning(self, 'Wrong answer!', 'Sorry, wrong answer. Try again :)', QtGui.QMessageBox.Ok)
                self.stackedWidget.setCurrentIndex(1)
                self.guessBox.clear()
                self.counter = 0
                self.mylist = []
                self.makelist()
                self.addnum()
                self.qt_x = self.mylist[self.counter]
            
    def qt_startGame(self):
        self.stackedWidget.setCurrentIndex(2)
        self.qt_x = self.mylist[self.counter]
        self.qt_doGame(self.qt_x)

    def qt_doGame(self, x):
        end = 1000*(limits[self.mylist.index(x)])
        self.popNum(x)
        self.myTimer.start(end)

    def qt_endGame(self):
        self.timeoutmsg = QtGui.QMessageBox.warning(self, 'Time\'s up!', 'Sorry! You ran out of time.', QtGui.QMessageBox.Ok)
        self.stackedWidget.setCurrentIndex(1)
        self.myTimer.stop()
        self.guessBox.clear()
        self.counter = 0
        self.mylist = []
        self.makelist()
        self.addnum()
        self.qt_x = self.mylist[self.counter]
    
    def youWin(self):
        self.myTimer.stop()
        self.movie.start()
        self.stackedWidget.setCurrentIndex(3)
        self.winmsg.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Ui_MainWindow()
    GUI.show()
    sys.exit(app.exec_())
    
01:44:57 PM