from threading import Thread
from puzzle import * 
import time
from server import *
gamegrid = GameGrid()
gamegrid.init_grid()
gamegrid.init_matrix()
gamegrid.update_grid_cells()
input()
f = Thread(target = app.run)
f.start()

for i in range(200):
	print(i)
