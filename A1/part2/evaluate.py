# indexA: path, numbers, fringe
# Solution path returned
# Total number of nodes expanded
# Maximum size of fringe during runtime
# P:weight of each index

#compare two mazes
from __future__ import division 
def isHarder(indexA, indexB, P):
	p=0
	p = (len(indexB[0]) - len(indexA[0])) / len(indexA[0]) * P[0]
	p += (indexB[1] - indexA[1]) / indexA[1] * P[1]
	p += (indexA[2] - indexB[2]) / indexA[2] * P[2]
	return p>0

#compare final maze and original maze
def improve(indexA,indexB,P):
	p=0
	p = (len(indexB[0]) - len(indexA[0])) / len(indexA[0]) * P[0]
	p += (indexB[1] - indexA[1]) / indexA[1] * P[1]
	p += (indexA[2] - indexB[2]) / indexA[2] * P[2]
	return p
