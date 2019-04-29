#!/usr/bin/python
#coding: utf-8
###	generate a maze with two-dimensional array, if maze[i][j] == 0,this is a wall
###	maze is the maze matrix, walls save wall's position in tuple
import random
from numpy import *

def mazeGenerate(dim,p):
	if p > 1 or p <= 0:
		print "please enter a valid p"
		return
	cols = rows = dim
	maze = [[0 for col in range(cols)] for row in range(rows)]
	walls = []
	for i in range(0,rows):
		for j in range(0,cols):
			maze[i][j] = random.uniform(0,1)
			if maze[i][j] <= p:
				if (i == 0 and j == 0) or (i == rows-1 and j == cols-1):
					maze[i][j] = 1
				else:
					maze[i][j] = 0
					walls.append((i,j))
			else:
				maze[i][j] = 1
	return walls

