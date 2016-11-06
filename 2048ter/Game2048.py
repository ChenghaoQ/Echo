import os
from GameField import *


class G2048():


	def __init__(self,GameField):
		self.game_field = GameField()

	def game_init(self):
		self.game_field.reset()
		os.system('clear')
		self.game_field.draw()



	def play_with_action(self,action):

		if self.game_field.move(action):
			if self.game_field.is_win():
				return 'You win'
			if self.game_field.is_gameover():
				return 'Gameover'
		else:
			return 'Cannot move this way'

		os.system('clear')
		self.game_field.draw()
