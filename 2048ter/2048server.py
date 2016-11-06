import logging
from random import randint
from flask import Flask,render_template
from flask_ask import Ask,statement,question,session
app = Flask(__name__)
ask = Ask(app,"/")
#ogging.getLogger("flask_ask").setLevel(logging.DEBUG)

from Game2048 import *
game_board = G2048(GameField)


@ask.launch
def new_game():
	welcome_msg = "welcome to 2 0 4 8,say yes to begin "
	return question(welcome_msg)

@ask.intent('YesIntent')
def next_round():
	ins_msg = "Please say the direction to move"
	game_board.game_init()
	return question(ins_msg)


@ask.intent("AnswerIntent",convert ={'direction':str})
def answer(direction):
	action={'up':'Up','left':'Left','down':'Down','right':'Right'}
	game_board.play_with_action(action[direction])		
	return question('')

if __name__ =='__main__':
	app.run()










