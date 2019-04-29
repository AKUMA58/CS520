#!/usr/bin/python
#coding: utf-8
##	generate a maze with two-dimensional array, if maze[i][j] == 0,this is a wall
##	maze is the maze matrix, walls save wall's position in tuple
import random
import math
import heapq
import time

def in_close(close,successor):
	for item in close:
		if item[1] == successor:
			return True
	return False

def in_open(open_list,successor):
	for i,item in enumerate(open_list):
		if item[1] == successor:
			return i,True
	return None, False

def a_star(dim,walls):
	open_list = []
	close = []
	parent = [] #path and parent
	attempt = [] #no. of attempt nodes

	# fn(evaluate function) is made of tuple (gn + hn, gn) for convenience
	#fn = (abs(dim-0) + abs(dim-0),0) #mahattan
	fn = (math.sqrt((dim-0)**2+(dim-0)**2),0) #euclidean

	heapq.heappush(open_list,(fn,(0,0))) #priority queue, openlist = [(gn + hn, gn),(x,y),......],x,y is node's potision
	while open_list:
		current_node = heapq.heappop(open_list)
		if current_node[1] == (dim-1,dim-1):
			parent.append(current_node[1])
			return parent,len(set(attempt))
		close.append(current_node)

		attempt.append(current_node[1])

		#find succesor
		directions = [(-1,0),(0,1),(1,0),(0,-1)]
		for item in directions:
			x_new, y_new = current_node[1][0] + item[0], current_node[1][1] + item[1]
			successor = (x_new, y_new)
			if (x_new, y_new) in walls:
				continue
			if x_new < 0 or x_new > dim-1 or y_new < 0 or y_new > dim-1:
				continue
			if in_close(close,successor):
				attempt.append(successor)
				continue

			#temp_fn = (new_fn, new_gn); new_fn = new_gn + new_hn = gn + 1 + new_hn
			temp_fn = (fn[0] + 1 + math.sqrt((dim - x_new )**2+(dim - y_new)**2),fn[1] + 1)	
			#temp_fn = (fn[0] + 1 + abs(dim - x_new) + abs(dim - y_new),fn[1] + 1) 

			i = in_open(open_list,successor)[0]
			attempt.append(successor)
			if i:
				if current_node[0][1] > temp_fn:
					open_list[i][0] = temp_fn
				continue
			heapq.heappush(open_list,(temp_fn,successor))
		parent.append(current_node[1])
	return [],0 

def fringe(path):
	if path:
		tx = ty = fx = fy = 0
		for i in range(1,len(path)):
			if (path[i-1][0] == path[i][0]):
				tx += 1
				if cmp(tx,fx) == 1:
					fx = tx
			else:
				tx = 0
			if path[i-1][1] == path[i][1]:
				ty += 1
				if cmp(ty,fy) == 1:
					fy = ty
			else:
				ty = 0
		if cmp(fx,fy) == 1:
			fringe = fx
		else:
			fringe = fy
		return fringe
	return 0



#--test--#
def run_a_star(dim,walls):
	path,attempt_nodes = a_star(dim,walls)
	fringe_max = fringe(path)
	if path:
		return path,attempt_nodes,fringe_max
		#print "path:"
		#print path
		#print "no. of path:",len(path)
		#print "no. of attempt_nodes:",attempt_nodes
		#print "no. of max fringe:",fringe(path)

	return ([(0, 0)], 0, 0)



# p = 0.3
# dim = 120
# a = time.clock()
# run_a_star(dim,p)
# b = time.clock()
# print b-a



