import random
import csv
import math


inputfile=open("input_test.csv","r")
Ireader=csv.reader(inputfile)
colorfile=open("color_test.csv","r")
Creader=csv.reader(colorfile)
ip=[]
cl=[]
for row in Ireader:
	ip.append(row)
for row in Creader:
	cl.append(row)
num=random.randint(0,len(ip))
color=cl[num]
print ip[num]
sum=0
for i in range (9):
	sum+=int(ip[num][i])
Alpha=0.001
MEAN=float(sum)/float(9)
print MEAN
A0=0.1
B0=0.3
At=0
Bt=0
root1=(float(1)/float(2))/float(math.sqrt(2*(MEAN*float(A0)/float(0.21)-float(color[0]))**2+4*(MEAN*float(B0)/float(0.72)-float(color[1]))**2+3*(MEAN*float(1-A0-B0)/float(0.07)-float(color[2]))**2))
x=Alpha*root1*(4*(MEAN*(float(A0)/float(0.21))-float(color[0]))*(MEAN/float(0.21))-6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07)))
y=Alpha*root1*(8*(MEAN*(float(B0)/float(0.72))-float(color[1]))*(MEAN/float(0.72))-6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07)))
At1=A0-x
Bt1=B0-y
while math.sqrt((At1-At)**2+(Bt1-Bt)**2)>0.01:
	At=At1
	Bt=Bt1
	root=(float(1)/float(2))/float(math.sqrt(2*(MEAN*float(At)/float(0.21)-float(color[0]))**2+4*(MEAN*float(Bt)/float(0.72)-float(color[1]))**2+3*(MEAN*float(1-At-Bt)/float(0.07)-float(color[2]))**2))
	At1=At-Alpha*root*(4*(MEAN*(float(At)/float(0.21))-float(color[0]))*(MEAN/float(0.21))-6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07)))
	Bt1=Bt-Alpha*root*(8*(MEAN*(float(Bt)/float(0.72))-float(color[1]))*(MEAN/float(0.72))-6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07)))
	print At1,At
	print Bt1,Bt
	print 4*(MEAN*(float(At)/float(0.21))-float(color[0]))*(MEAN/float(0.21))
	print 6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07))
	print 4*(MEAN*(float(At)/float(0.21))-float(color[0]))*(MEAN/float(0.21))-6*(MEAN*(float(1-A0-B0)/float(0.07))-float(color[2]))*(MEAN/float(0.07))
	print root
	print MEAN*(float(At)/float(0.21))
	print float(math.sqrt(2*(MEAN*float(At)/float(0.21)-float(color[0]))**2+4*(MEAN*float(Bt)/float(0.72)-float(color[1]))**2+3*(MEAN*float(1-At-Bt)/float(0.07)-float(color[2]))**2))
	print "----------------"