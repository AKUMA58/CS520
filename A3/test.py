def iiii(a):
	if a>3:
		return a

b=[1,4,3,6,2,5]
c=[]
for i in range (len(b)):
	c.append(iiii(b[i]))

num=0
for j in range (len(c)):
	if c[j-num]==None:
		c.pop(j-num)
		num+=1

print len(c)
print c

def aa((i,j)):
	d.append(((i+1,j+2),0))
	d.append(((i+2,j+3),1))
	
d=[]
aa((1,1))
d.pop(0)
print d
print d[0][0]

def dsa(a):
	if a>3:
		return (1,2)
	else:
		return -1

d=[]
for i in range (len(b)):
	c=dsa(b[i])
	if c==-1:
		print "sb"
	else:
		d.append(c)
print d


