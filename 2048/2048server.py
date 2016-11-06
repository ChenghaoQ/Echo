import logging
from random import randint
from flask import Flask,render_template
from flask_ask import Ask,statement,question,session
app = Flask(__name__)
ask = Ask(app,"/")
#ogging.getLogger("flask_ask").setLevel(logging.DEBUG)

from puzzle import *



@ask.launch
def new_game():
	welcome_msg = "welcome to 20 48,say yes to begin, say instruction for instruction "
	return question(welcome_msg)

@ask.intent('YesIntent')
def next_round():
	ins_msg = "Please say the direction to move"
	#gamegrid.init_grid()
	#gamegrid.init_matrix()
	#gamegrid.update_grid_cells()
	return question(ins_msg)


@ask.intent("AnswerIntent",convert ={'direction':str})
def answer(direction):
	#action={'up':'Up','left':'Left','down':'Down','right':'Right'}
	print(direction)

	gamegrid.key_down(direction)			
	return question('Roger that')






if __name__ =='__main__':
	#app.run()






