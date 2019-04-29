 
from collections import Counter
from kmeans import Kmeans

class GreyToMap:
	def __init__(self,k1,k2):
		self.greyd=None
		self.colord=None
		self.greyk=None
		self.colork=None
		self.greypt=None
		self.colorpt=None
		self.map_=dict()
		self.map=dict()
		self.num=None
		self.init(k1,k2)


	def init(self,k1,k2):
		Kg=Kmeans("input_test.csv",k1)
		Kg.run()
		self.greyd=Kg.data
		self.greypt=Kg.ptCenter
		Kc=Kmeans("color_test.csv",k2)
		Kc.run()
		self.colord=Kc.data
		self.colorpt=Kc.ptCenter
		self.num=len(self.greyd)
		for key in Kg.centers:
			self.map_[key] = list()


	def grey2color(self):
		for p in range(self.num):
			grey=self.greypt[tuple(self.greyd[p])]
			color=self.colorpt[tuple(self.colord[p])]
			self.map_[tuple(grey)].append(color)
		for g in self.map_:
			self.map[g]=Counter(self.map_[g]).most_common(1)[0][0]
		return self.map
# 
# m=GreyToMap(3,3)
# m.grey2color()