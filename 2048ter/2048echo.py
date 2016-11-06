import os
from GameField import *
actions=['Up','Left','Down','Right','Restart','Exit']
 

def init(): # reset the game field and restart the game
	game_field.reset() # using game_field not GameField because there is a statement below
	return 'Game'	#can we use dictionary like this? why>

def not_game(state): #Not game status is for gameover or win after game
	game_field.draw()   #other than self, there is another variable in it
	action = get_user_action()#where is this
	response = defaultdict(lambda:state) #default is current status, no action will keep the current status
	response['Restart'],response['Exit'] ='Init','Exit' # Restart need to  init again, exit just exit
	
	return response[action]#Return the users respones'''


def game():
	os.system('clear')
	game_field.draw() # draw the current field status
	action=get_user_action()#get useer action

	if action =='Restart':
		return 'Init'
	if action =='Exit':
		return 'Exit'
	if game_field.move(action): # move successful ( move not none)
		if game_field.is_win():
			return 'Win'
		if game_field.is_gameover():
			return 'Gameover'
	return 'Game'

state_actions ={'Init':init,  #put state into a dictionary
		'Win':lambda:not_game('Win'),
		'Gameover':lambda:not_game('Gameover'),
		'Game':game
	}

#curses.use_default_colors()
 # how to change to Mac

state='Init' # initialize the state

# circulated the status machine
while state !='Exit':
	state = state_actions[state]() # state_action[state] from dictionary actually is a function, so put the argument in the ()	



if __name__ == '__main__':

    app.run(debug=True)




#License

#本作品在 GFDL1.2 协议下授权使用,ekCit作品
