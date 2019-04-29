import csv
from math import exp,log1p,sqrt
from random import random,randint
import numpy as np
import sys
from sklearn.cluster import KMeans
from kmeans import Kmeans
from GreyToColorMap import GreyToMap
from sklearn.metrics.pairwise import euclidean_distances

class Logistic:
	def __init__(self,k1,k2):
		self.A=[[0]*9]*3
		self.alpha=0.01
		self.greyd=None
		self.colord=None
		self.greyc=[]
		self.colorc=[]
		self.indexmap=dict()
		self.greypt=None
		self.colorpt=None
		self.m=None
		self.map=dict()
		self.init(k1,k2)
		self.max=100
		self.minLoss=0.01
		self.Loss=None


	def init(self,k1,k2):
		Kg=Kmeans("input_test.csv",k1)
		Kg.run()
		self.greyd=Kg.data
		self.greypt=Kg.ptCenter
		Kc=Kmeans("color_test.csv",k2)
		Kc.run()
		self.colord=Kc.data
		self.colorpt=Kc.ptCenter
		self.m=GreyToMap(k1,k2)
		self.map=self.m.grey2color()
		self.loss=None
		self.initA()

	def initA(self):
		for i in range(3):
			for j in range(9):
				self.A[i][j]=round(0.01*random(),5)
		print self.A
		self.processdata()

	def processdata(self):
		for ind in range(len(self.greyd)):
			p=self.greyd[ind]
			x=self.greypt[tuple(p)]
			# y=self.map[tuple(x)]
			y=self.colorpt[tuple(self.colord[ind])]
			x=[float(x_)/float(255) for x_ in x]# 1 by 9 list
			y=[float(y_)/float(255) for y_ in y] # 1 by 3 list
			self.greyc.append(x)
			self.colorc.append(y)
	# def color2index(self):
	# 	ind=0
	# 	for key in self.map:
	# 		color=self.map[key]
	# 		if color in self.indexmap:
	# 			continue
	# 		self.indexmap[tuple(color)]=ind
	# 		ind+=1
	# 	return self.indexmap

	def sumGrad(self):#3 by 9
		G=0
		ind=randint(0,len(self.greyd)-1)
		# for p in self.greyd:
		# 	x=self.greypt[tuple(p)] # 1 by 9 list
		# 	y=self.map[tuple(x)] # 1 by 3 list
		# 	f=self.fax(x)
		# 	G+=np.dot((np.array([f])-np.array([y])).transpose(),np.array([x])) #array
		# p=self.greyd[ind]
		# x=self.greypt[tuple(p)] # 1 by 9 list
		# y=self.map[tuple(x)] # 1 by 3 list
		x=self.greyc[ind]
		y=self.colorc[ind]
		f=self.fax(x)
		G=np.dot((np.array([f])-np.array([y])).transpose(),np.array([x]))#array
		G=np.round(G,decimals=5)
		# print f
		# print y
		# print (np.array([f])-np.array([y]))
		# print G
		return G

	def fax(self,x): # 3 by 1
		f=list()
		temp=np.dot(self.A,np.array([x]).transpose())
		temp=np.round(temp,decimals=5)
		# print temp
		for i in range (3):
			f.append(round(float(1)/float(1+exp(-temp[i])),5))
		# print f
		return f

	def CalLoss(self):
		L=0
		for ind in range(len(self.greyc)):
			x=self.greyc[ind]
			y=self.colorc[ind]
			f=self.fax(x) #list
			#Loss function on numerical values
			# L+=(np.array([f])-np.array([y]))**2
			#color difference
			L+=sqrt(2*(f[0]-y[0])**2+4*(f[1]-y[1])**2+3*(f[2]-y[2])**2)
		# L=np.divide(L,len(self.greyd))
		self.Loss=np.round(L,decimals=5)
		# self.Loss=np.sqrt(np.sum(self.Loss**2))

	def updateA(self):# 3 by 9
		r=0
		while True:
			m =len(self.greyd)//5
			while m>0:
				Ak=np.array(self.A)
				self.A-=self.alpha*self.sumGrad() #array
				self.A=np.round(self.A,decimals=5)
				m-=1
			# deltaA=(self.A-Ak)**2
			# 	# print deltaA
			# deltaA = np.sqrt(np.sum(deltaA))
			# deltaA = np.round(deltaA,decimals=2)
			# print self.A
			self.CalLoss()
			print self.Loss
			r+=1
			if np.divide(self.Loss,len(self.greyd)) <=self.minLoss *len(self.geryd):
				print r
				break
		return self.A


k = Logistic(5,5)
weight=k.updateA()
print weight
