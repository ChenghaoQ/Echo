import logging
from random import randint
from flask import Flask,render_template
from flask_ask import Ask,statement,question,session
app = Flask(__name__)
ask = Ask(app,"/")
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

from puzzle import *
from threading import Thread
from time import sleep

direc = ''
gamegrid =GameGrid()

@ask.launch
def new_game():
	welcome_msg = "welcome to 20 48,say yes to begin, say instruction for instruction "
	
	return question(welcome_msg)

@ask.intent('YesIntent')
def next_round():
	ins_msg = "Please say the direction to move"
	return question(ins_msg)


@ask.intent("AnswerIntent",convert ={'direction':str})
def answer(direction):
	global direc
	
	try:
		direc = direction
	except:
		pass
		
	return question('')


def listener():
	global direc

	global gamegrid
	tmp = direc
	while True:
		try:

			if direc != tmp:
				
				gamegrid.key_down(direc)
				tmp = direc
			if direc == 'stop':
				break
		
		except:
			pass
		




gamegrid.init_grid()
gamegrid.init_matrix()
gamegrid.update_grid_cells()
input()


f = Thread(target = app.run)
f.start()
listener()
f.join()








