from __future__ import division 
from random import *
from map import *
import time
class MovingTarget:
	def __init__(self):
		self.m = None
		self.graph = None
		self.target = None
		self.targetPath = None
		self.fn = None
		self.n = None
		self.indexOfTargetPath = 0
		self.init()
	def init(self):
		self.m = Map()
		self.graph = self.m.map
		self.target = self.m.target
		self.targetPath = []
		self.fn = self.m.fn
		self.n = self.m.n

	def move_target(self,target_position,choice):
		now_type = self.graph[target_position]['type']
		neighbors = list(self.graph[target_position]['neighbours'])
		if choice == 'rule2' and self.indexOfTargetPath <= len(self.targetPath) - 1:
			neighbor_position = self.targetPath[self.indexOfTargetPath]
			self.indexOfTargetPath += 1
		else:
			neighbor_position = neighbors[randint(0,len(neighbors)-1)]
		neighbor_type =self.graph[neighbor_position].get('type')
		Info=[]
		Info.append(now_type)
		Info.append(neighbor_type)
		if choice == 'rule1':
			self.targetPath.append(neighbor_position)
		return neighbor_position,Info

	def firsttest (self,point,ft,st):
		count=0
		for nei in self.graph[point]['neighbours']:
			if self.graph[nei]['type'] == ft:
				count += 1
				break
		for nei in self.graph[point]['neighbours']:
			if self.graph[nei]['type'] == st:
				count += 1
				break
		if count == 2:
			return True
	#point is a location,ft is first from terrain,st is second to terrain
	def update(self,pointV,Info):
		tempPointV = dict(pointV)
		pointV = dict()
		for k,v in tempPointV.iteritems():
			temp = Info[1] if self.graph[k]['type'] == Info[0] else Info[0]
			num=0
			for nei in self.graph[k]['neighbours']:
				if self.graph[nei]['type'] == temp:
					num+=1
			for nei in self.graph[k]['neighbours']:
				if self.graph[nei]['type'] == temp:
					if nei not in pointV:
						pointV[nei] = v/num
					else:
						pointV[nei] += v/num

	def movingtarget(self,choice):
		if choice == 'rule1':
			self.targetPath = []
			self.indexOfTargetPath = 0
		success=0
		tsterrain=[]
		terrain=[]
		point=[]
		pointV=dict()
		numclick=0
		if choice == 'rule1':
			rx = randint(0,self.n-1)
			ry = randint(0,self.n-1)
			target=(rx,ry)
			self.targetPath.append(target)
		else:
			target = self.targetPath[self.indexOfTargetPath]
			self.indexOfTargetPath += 1
		#print target
		

		clickpoint=(randint(0,self.n-1),randint(0,self.n-1))
		#print clickpoint
		#print 'a'
		numclick+=1
		p = random()
		if clickpoint==target and p > self.fn[self.graph[clickpoint]['type']]:
			success=1
			return numclick
		else:
			target,Info=self.move_target(target,choice)

		#Info0 -first information
		Info0=Info
		clickpoint=(randint(0,self.n-1),randint(0,self.n-1))
		# print target
		# print clickpoint
		# print 'a'
		numclick+=1
		p = random()
		if clickpoint==target and p > self.fn[self.graph[clickpoint]['type']]:
			success=1
			return numclick
		else:
			target,Info=self.move_target(target,choice)

		#Info -second information
		#tsterrain -terrain appears twice
		for i in range (2):
			for j in range (2):
				if Info0[i]==Info[j]:
					if len(tsterrain)==0:
						tsterrain.append(Info0[i])
					elif tsterrain[0]!=Info0[i]:
						tsterrain.append(Info0[i])

		#point -last one point
		for i in range (len(tsterrain)):
			count=0
			for key in self.graph:
				if self.graph[key]['type'] == tsterrain[i]:
					point.append(key)
					count+=1
			terrain.append((tsterrain[i],count))
		num=0
		#find first from terrain,find second to terrain
		for i in range (len(point)):
			if i<tsterrain[0][1]:
				if tsterrain[0][0]==Info0[0]:
					ft=Info[1]
				else:
					ft=Info[0]
				if tsterrain[0][0]==Info[0]:
					st=Info[1]
				else:
					st=Info[0]
				result=self.firsttest(point[i-num],ft,st)
				if result==None:
					point.pop(i-num)
					num+=1
			else:
				if tsterrain[1][0]==Info0[0]:
					ft=Info[1]
				else:
					ft=Info[0]
				if tsterrain[1][0]==Info[0]:
					st=Info[1]
				else:
					st=Info[0]
				result=self.firsttest(point[i],ft,st)
				if result==None:
					point.pop(i-num)
					num+=1

		#point is now last points with probability
		#pointV -first column is point,second column is value
		for p in point:
			pointV[p] = 1 if choice == 'rule1' else 1-self.fn[self.graph[p]['type']]
		self.update(pointV,Info)
		clickpoint=max(pointV.items(), key = lambda item: item[1])[0]
		# print target
		# print clickpoint
		# print 'a'
		numclick+=1
		p = random()
		if clickpoint==target and p > self.fn[self.graph[clickpoint]['type']]:
			success=1
		else:
			for k in pointV:
				if k==clickpoint:
					pointV[k]*=self.fn[self.graph[clickpoint]['type']]

		#pointV -first column is point,second column is value
		while success==0:
			target,Info=self.move_target(target,choice)
			self.update(pointV,Info)
			clickpoint=max(pointV.items(), key = lambda item: item[1])[0]
			numclick+=1
			# print target
			# print clickpoint
			# print 'a'
			p = random()
			if clickpoint==target and p > self.fn[self.graph[clickpoint]['type']]:
				success=1
			else:
				for k in pointV:
					if k==clickpoint:
						pointV[k]*=self.fn[self.graph[clickpoint]['type']]
			# print len(pointV)
			print numclick
		return numclick

avg1=0
avg2=0
n=500
mv = MovingTarget()
a=time.clock()
for i in range (n):
	avg1+=mv.movingtarget('rule1')
	avg2+=mv.movingtarget('rule2') 
	print('------------------------------------')
b=time.clock()
print avg1/n
print avg2/n
print b-a




