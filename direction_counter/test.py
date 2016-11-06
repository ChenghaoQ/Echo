import logging
from random import randint

from flask import Flask,render_template
from flask_ask import Ask,statement,question,session


from testcounter import Counter
app = Flask(__name__)
ask = Ask(app,"/")
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

dir_count=Counter()

@ask.launch
def new_game():
	welcome_msg = "welcome to direction,say yes to begin "
	return question(welcome_msg)

@ask.intent('YesIntent')
def next_round():
	ins_msg = "Please say a direction"
	return question(ins_msg)


@ask.intent("AnswerIntent",convert ={'direction':str})
def answer(direction):
	dir_count.direction_count(direction)


	print('--------',direction,'------------,dir_count.counter')
	msg=''	
	#msg = direction+',right?'+"It's the number %d direction you said"%dir_count.counter
	return question(msg)

if __name__ =='__main__':
	app.run()






