from random import random,randint
import logging
import time
import operator
from math import *
from map import Map
logging.basicConfig(level=logging.INFO)


class MoveToTarget:
	def __init__(self):
		self.belief= None
		self.m = Map()
		self.map = None
		self.fn = self.m.fn
		self.target = None
		self.cells = dict()
		self.count = None
		self.maxSearchTimes = None
		self.init()
		self.targetcount = 0

	def init(self):
		# self.belief={'flat':1,'hilly':1,'forested':1,'cave':1}
		self.map = dict(self.m.map)
		# group type
		self.cells['flat'] = list()
		self.cells['hilly'] = list()
		self.cells['forested'] = list()
		self.cells['cave'] = list()
		for key in self.map:
			self.cells[self.map[key]['type']].append(key)
		self.count = 0
		self.maxSearchTimes = 100000
		self.targetcount  = 0


	def searchResult(self, position):
		if self.target != position:
			return False
		else:
			self.targetcount += 1
			p = random()
			terrain = self.map[position]['type']
			if p < self.fn[terrain]:
				return False
			else:
				return True
	def setTarget(self, terrain):
		ranp=randint(0,len(self.cells[terrain])-1)
		self.target=self.cells[terrain][ranp]
		self.m.target=self.target
		return 

	def comparison(self,position,opt,state):
		candi=dict()
		candi[opt]=self.pcost(position,opt)
		dist=dict() #distance betwen nei and opt
		for nei in self.map[position]['neighbours']:
				candi[nei]=self.pcost(position,nei)
				dist[nei]=abs(nei[0]-opt[0])+abs(nei[1]-opt[1])
		if state=='move':
			candi[position]=self.pcost(position,position)
		next_best = max(candi.iteritems(), key=operator.itemgetter(1))[0]
		if next_best!= opt:
			next_posi = min(dist.iteritems(), key=operator.itemgetter(1))[0]
		else:
			next_posi=next_best
		# print candi
		# print('opt',opt)
		# print(next_posi,candi[next_posi])
		return next_posi

	def pcost(self,position,candi):
		cost=abs(position[0]-candi[0])+abs(position[1]-candi[1])+1
		p_cost=float(float(self.map[candi]['p'])/float(cost))
		# print (self.map[candi]['p'],cost)
		# print('p_cost',p_cost)
		return p_cost

	def run(self,choice):
		self.init()
		if choice=='rule2':
			terrain = 'flat'
		else:
			terrain=['flat','hilly','forested','cave'][randint(0,3)]
		position=self.cells[terrain][0]
		while self.maxSearchTimes > 0:
			if self.searchResult(position):
				# print('success = ', self.count)
				# print('target = ', self.target, self.map[self.target])
				# print('terrain = ', terrain)
				# print('targetcount = ', self.targetcount)
				return self.count
			else:
				self.count += 1
				self.maxSearchTimes -= 1
				# print('Search!')
				factor = self.map[position]['p']*self.fn[self.map[position]['type']]
				# update p value
				if choice == 'rule2':
					# for rule two
					factor *= (1-self.fn[self.map[position]['type']])
				self.map[position]['p'] = factor
				p=0
				for key in self.map:
					temp_p=self.map[key]['p']
					if temp_p>p:
						p=temp_p
						opt=key
				temp_next=self.comparison(position,opt,'search')
				curr=position
				#move
				while temp_next!=curr:
					self.count+=1
					# print('current position:',curr)
					curr=temp_next #move one step
					temp_next=self.comparison(curr,opt,'move')# next cell to move
					# print('next_posi',temp_next,'target',self.target,self.map[self.target]['type'])
				position=temp_next	
			# if self.searchResult(self.cells[terrain][len(self.cells[terrain])-1]):
			# 	# print('success = ', self.self.count)
			# 	# print('target = ', self.target, self.map[self.target])
			# 	# print('terrain = ', terrain)
			# 	# print('targetself.count = ', self.targetself.count)
			# 	return self.self.count
			# else:
			# 	self.maxSearchTimes -= 1
			# 	self.self.count += 1
			# 	# for rule one
			# 	factor = self.fn[terrain]
			# 	if choice == 'rule2':
			# 		# for rule two
			# 		factor *= (1-self.fn[terrain])
			# 	self.belief[terrain] *= factor
			# 	terrain = max(self.belief.iteritems(), key=operator.itemgetter(1))[0]

st = MoveToTarget()
# av1 = 0
# av2 = 0
n = 1
terrain = ['flat', 'hilly', 'forested', 'cave']
for ter in terrain:
	print('---------------------ter = ',ter,'------------------------')
	av1 = 0
	av2 = 0
	st.setTarget(ter)
	for i in range(n):
		print('----------')
		st.run('rule1') 
		av1 += st.count
		st.run('rule2')
		av2 += st.count
	print('average number of search by rule 1 =',av1//n) 
	print('average number of search by rule 2 =',av2//n)