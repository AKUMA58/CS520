import csv
from math import sqrt
from random import randint
import numpy as np
import sys

from sklearn.cluster import KMeans

class Kmeans:

	def __init__(self, filename, k):
		self.filename = filename
		self.k = k
		self.data = self.readData()
		self.centers = self.randomCenters()
		self.ptCenter = dict()
		self.init()

	def init(self):
		for key in self.data:
			self.ptCenter[tuple(key)] = []

	def randomCenters(self):
		centers = dict()
		temp = set()
		for i in range(self.k):
			r = randint(0,len(self.data)-1)
			while r in temp:
				r = randint(0,len(self.data)-1)
			centers[tuple(self.data[i])] = []
			temp.add(r)
		return centers

	def getCenters(self):
		self.run()
		return self.centers.keys()




	def readData(self):
		with open(self.filename,"rb") as f:
			reader = csv.reader(f)
			input_list = list(reader)
		for i in range(len(input_list)):
			for j in range(len(input_list[0])):
				input_list[i][j] = int(input_list[i][j])
		return input_list

	def distance(self,p1, p2):
		dis = 0
		for i in range(len(p1)):
			dis += (p1[i]-p2[i])**2
		return dis

	def classify(self):
		change = 0
		for pt in self.data:
			dist = sys.maxint
			temp = tuple()
			for key in self.centers:
				if(self.distance(key, pt) < dist):
					dist = self.distance(key, pt)
					temp = key
			if(self.ptCenter[tuple(pt)] == temp):
				change += 1
			self.ptCenter[tuple(pt)] = temp
			self.centers[temp].append(pt)
		# terminate condition
		if(change == len(self.data)):
			return 'END'
		# update center
		self.updateCenter()

	def run(self):
		i = 0
		while True:
			i += 1
			res = self.classify()
			if res == 'END':
				# print i
				return

	def error(self):
		errorSum = 0
		for key in self.ptCenter:
			errorSum += self.distance(key, self.ptCenter[key])
		return errorSum



	def updateCenter(self):
		for key in dict(self.centers):
			temp = self.centers[key]
			newKey = []
			for i in range(len(self.data[0])):
				tempSum = 0
				for j in range(len(temp)):
					tempSum += temp[j][i]
				newKey.append(round(float(tempSum) / float(len(temp)),2))
			del self.centers[key]
			self.centers[tuple(newKey)] = []



# print type (list(np.sum([[1,1]], axis=0))[0])
# kmeans = Kmeans("input.csv",50)
# centers = kmeans.getCenters()
# # print centers

# # test
# # skmeans = KMeans(n_clusters=50, random_state=0).fit(kmeans.data)
# # print  skmeans.cluster_centers_
# # print skmeans.inertia_
# print kmeans.error()




