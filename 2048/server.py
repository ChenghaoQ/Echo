import logging
from flask import Flask,render_template
from flask_ask import Ask,statement,question,session
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)
from puzzle import *
from threading import Thread
from time import sleep


app = Flask(__name__)
ask = Ask(app,"/")
gamegrid=None
status = 'not_yet'


@ask.launch
def welcome():
	welcome_msg = "welcome to 20 48,say yes to begin, say instruction for instruction "
	
	return question(welcome_msg)

@ask.intent('YesIntent')
def start_instruction():

	global status
	global gamegrid
	if status == 'not_yet':
		gamegrid =GameGrid()
		ins_msg = "Please say the direction to move"
		status = 'in_game'
		return question(ins_msg)
	return question("already in game")


@ask.intent("AnswerIntent",convert ={'action':str})
def game(action):
	global direc
	global gamegrid
	if action in ['left','right','up','down']:
		try:
			#direc = action
			gamegrid.key_down(action)
			
		except:
			pass

		return question('')

	return question('invalid action,please try again')

"""

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
		

"""


#gamegrid.init_grid()
#gamegrid.init_matrix()
#gamegrid.update_grid_cells()
#input()


f = Thread(target = app.run)
f.start()
#listener()
f.join()








