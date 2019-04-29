#To use this execution, first write "from DFS import *",then use DFSrun fuction.Input should be DFSrun(wall,dim).Wall is list of walls,dim is length of maze.Output will be "path,nodes,fringe".Path is path of result,nodes is nodes expanded,fringe is maximun size of fringe
#It will write result of path to a file "DFSdata.txt"

import random
from numpy import *

#current point moves to next point,record moving direction
def Forward (k):
	direction=0
#right
	if k==-2: 
		testpoint[0]=point[0]
		testpoint[1]=point[1]+1
		direction=-2
#down
	if k==-1:
		testpoint[0]=point[0]+1
		testpoint[1]=point[1]
		direction=-1
#left
	if k==2:
		testpoint[0]=point[0]
		testpoint[1]=point[1]-1
		direction=2
#up
	if k==1:
		testpoint[0]=point[0]-1
		testpoint[1]=point[1]
		direction=1
	return direction

#according to moving direction,move back to parent point
def Backward (k):
#left
	if k==-2: 
		point[0]=point[0]
		point[1]=point[1]-1
		direction=-2
#up
	if k==-1:
		point[0]=point[0]-1
		point[1]=point[1]
		direction=-1
#right
	if k==2:
		point[0]=point[0]
		point[1]=point[1]+1
		direction=2
#down
	if k==1:
		point[0]=point[0]+1
		point[1]=point[1]
		direction=1

direction=0
point=[0,0]
testpoint=[0,0]
move=1
lastdirection=0
answer=0
path=[]
nodes=[]
path.append((0,0))

#DFS running function,use testmatrix to represent wall,empty point and direction of each expanded point's parent point

def DFSrun(wall,dim):		
	end=0
	fs=1
	fringe=0
	ln=len(wall)
	testmatrix=[[0 for col in range(dim)] for row in range(dim)]
	
	if len(path)>1:
		path[:]=[]
		path.append((0,0))
		nodes[:]=[]
		point[0]=0
		point[1]=0
		for i in range (dim):
			for j in range (dim):
				testmatrix[i][j]=0

#represent walls in the maze	
	for i in range (ln):
		a=wall[i][0]
		b=wall[i][1]
		testmatrix[a][b]=3

	while end==0:
		full=1
		for i in range(-2,3):
			move=1
			lastdirection=testmatrix[point[0]][point[1]]
			if i==(0-lastdirection):
				move=0
			else:	
				direction=Forward(i)
				if (testpoint[0]<0 or testpoint[1]<0 or testpoint[0]==dim or testpoint[1]==dim):
					move=0
					continue
				tx=testpoint[0]
				ty=testpoint[1]
				if testmatrix[tx][ty]==0:
					move=1
				else:
					move=0
				for j in range(0,ln):
					if wall[j]==(testpoint[0],testpoint[1]):
						move=0	
			if move==1:
				point[0]=testpoint[0]
				point[1]=testpoint[1]
				path.append((point[0],point[1]))
				p=point[0]
				q=point[1]
				testmatrix[p][q]=direction
				if (point[0]==dim-1 and point[1]==dim-1):
					end=1
					answer=1
				break
		if move==0:
			x=point[0]
			y=point[1]
			if (point[0]==0 and point[1]==0):
				end=1
				answer=0
				path[:]=[]
			else:
				path.pop()
			Backward(testmatrix[x][y])
	if answer==0:
		file=open('DFSdata.txt','w')
		file.write("There is no path.\n")
		file.close()
	else:
		nodes.append((0,0))
		for i in range (dim):
			for j in range (dim):
				if testmatrix[i][j]!=0 and testmatrix[i][j]!=3:
					nodes.append((i,j))
		if path[1][0]==path[0][0]:
			rc=1
		else:
			rc=2
		for n in range (1,len(path)):
			if path[n][0]==path[n-1][0]:
				now=1
			else:
				now=2
			if now!=rc:
				fe=n-1
				rc=now
				if fringe<(fe-fs+1):
					fringe=fe-fs+1
				fs=fe
		file=open('DFSdata.txt','a+')
		file.write(str(path))
		file.close()
	return path,len(nodes),fringe
	
def run_dfs(wall,dim):
	path, nodes, fringe = DFSrun(wall,dim)
	if path:
		return path, nodes, fringe
	return ([(0, 0)], 0, 0)


	