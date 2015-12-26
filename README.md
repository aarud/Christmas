This program is LINUX ONLY (certainly the terminal-based rands.py, and the UI version as well, as far as I know. QTimer may work on Windows but I haven't tried). 

It's a game that makes the player calculate squares really fast; it resets if time
runs out or a wrong answer is entered.

Description of files:
----scripts----
backup.sh
#do a backup from Squares.py to Squares_ui_bak.py
doSquares.sh
#Unneeded for you. Just runs the program. It was only created bc 
#the .desktop for the Squares.py script wouldn't work, so I had to make
#a .desktop from this script instead.
rands.py 
#the original script; terminal only.
Squares.py
#the program. Generate from .ui file with ~$ pyuic4 <src file> > <target file>
Squares_ui_bak.py
#backup of Squares
s2.py
#the program, numers [0-6] as problems; great for testing (who wants to square
#68 in a test program?)

----other----
giphy2.gif
#gif on the 'win' page
xpmas 
#pic for the icon


