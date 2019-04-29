from random import random,randint
import logging
import time
import operator
from map import Map
logging.basicConfig(level=logging.INFO)

class SkipToTarget:
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
		self.targetCount = 0

	def init(self):
		self.belief={'flat':1,'hilly':1,'forested':1,'cave':1}
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
		self.targetCount  = 0


	def searchResult(self, position):
		if self.target != position:
			return False
		else:
			self.targetCount += 1
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

	def run(self,choice):
		self.init()
		if choice=='rule2':
			terrain = 'flat'
		else:
			terrain=['flat','hilly','forested','cave'][randint(0,3)]
		while self.maxSearchTimes > 0:
			for i in range(len(self.cells[terrain])-1):
				if self.searchResult(self.cells[terrain][i]):
					# print('success = ', self.count)
					# print('target = ', self.target, self.map[self.target])
					# print('terrain = ', terrain)
					# print('targetCount = ', self.targetCount)
					return self.count
				else:
					self.count += 1
					self.maxSearchTimes -= 1
			if self.searchResult(self.cells[terrain][len(self.cells[terrain])-1]):
				# print('success = ', self.count)
				# print('target = ', self.target, self.map[self.target])
				# print('terrain = ', terrain)
				# print('targetCount = ', self.targetCount)
				return self.count
			else:
				self.maxSearchTimes -= 1
				self.count += 1
				# for rule one
				factor = self.fn[terrain]
				if choice == 'rule2':
					# for rule two
					factor *= (1-self.fn[terrain])
				self.belief[terrain] *= factor
				terrain = max(self.belief.iteritems(), key=operator.itemgetter(1))[0]

st = SkipToTarget()
# av1 = 0
# av2 = 0
n = 1000
terrain = ['flat', 'hilly', 'forested', 'cave']
for ter in terrain:
	print('---------------------ter = ',ter,'------------------------')
	av1 = 0
	av2 = 0
	st.setTarget(ter)
	for i in range(n):
		# print('----------')
		st.run('rule1') 
		av1 += st.count
		st.run('rule2')
		av2 += st.count
	print('average number of search by rule 1 =',av1//n) 
	print('average number of search by rule 2 =',av2//n) 













