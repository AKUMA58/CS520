import random
from DFS import *
from bfs import *
from a_star import *
from evaluate import *
from maze import *

dim,wall=maze()
print wall
testwall=[]
curwall=[]
maxwall=[]
path=[]
orgindex=[]
curindex=[]
tsindex=[]
maxindex=[]
exepath=[]
nodes=0
repath=[]
renodes=0
refringe=0
fringe=0
x=0
y=0
nx=0
ny=0
q=(3,6,0.5)
order=raw_input("choose search algorithm('quit' to end):")

#define number of "restart"
setno=5
if len(wall)<setno:
	NoRestart=len(wall)
else:
	NoRestart=setno

#according to order and wall,run function
def choose(o,wall):
	if o=="DFS":
		path,nodes,fringe=run_dfs(wall,dim)
	if o=="BFS":
		path,nodes,fringe=run_bfs(dim,wall)
	if o=="A*":
		path,nodes,fringe=run_a_star(dim,wall)
	return path,nodes,fringe

#test out of boundary
def test(a,b):
	if a<0 or b<0 or a>dim-1 or b>dim-1:
		return 1
	else:
		return 0

#add into or remove from wall list
def addsub(c,d,w):
	b=w
	if (c,d) in w:
		for j in range (len(w)):
			if w[j]==(c,d):
				a=j
		for i in range (0,a):
			b[i]=w[i]
		for i in range (a+1,len(w)):
			b[i-1]=w[i]
		b.pop()	
	else:
		b=w
		b.append((c,d))
	return b

#reset recording file
def reset(order):
	if order=="DFS":
		file=open('mazechangeDFS.txt','w+')
		file.truncate()
		file.close()
	if order=="BFS":
		file=open('mazechangeBFS.txt','w+')
		file.truncate()
		file.close()
	if order=="A*":
		file=open('mazechangeA_star.txt','w+')
		file.truncate()
		file.close()

#write results into recording file
def writeFile (o,wall):
	if o=="DFS":
		file=open('mazechangeDFS.txt','a+')
		file.write(str(wall))
		file.write("\n")
		file.close()
	if o=="BFS":
		file=open('mazechangeBFS.txt','a+')
		file.write(str(wall))
		file.write("\n")
		file.close()	
	if o=="A*":
		file=open('mazechangeA_star.txt','a+')
		file.write(str(wall))
		file.write("\n")
		file.close()

#running function
while order!="quit":
	if order!="BFS" and order!="DFS" and order!="A*":
		print "invalid order"
		print "valid order:BFS or DFS or A* or quit"
		order=raw_input("choose search algorithm('quit' to end):")
		break
	reset(order)
	end=0
	path,nodes,fringe=choose(order,wall)
	if len(path)<3:
		quit()
	curpath=path[:]
	curnodes=nodes
	curindex=(curpath,curnodes,fringe)
	orgindex=(curpath,curnodes,fringe)
	exepath=path[:]
	
#in each restart
	for n in range (NoRestart):
		dim,wall=maze()
		testwall=wall
		accept=0
		move=0
		print exepath

#find start point 
		while accept<1:
			if len(exepath)<3:
				end=1
				print "end"
				break
			fc=random.randint(1,len(exepath)-1)
			x=int(exepath[fc][0])
			y=int(exepath[fc][1])
			testwall.append((x,y))
			repath,renodes,refringe=choose(order,wall)
			if repath==[]:
				exepath.pop(fc)
				continue
			tsindex=(repath,renodes,refringe)
			if isHarder(curindex,tsindex,q):
				del curwall
				curwall=testwall[:]
				del maxwall
				maxwall=curwall[:]
				del curindex
				a=tsindex[0]
				a1=a[:]
				b=tsindex[1]
				c=tsindex[2]
				curindex=(a1,b,c)
				maxindex=(a1,b,c)
				accept=1
				testwall.pop()
				print "success"
			else:
				testwall.pop()
			if len(exepath)<1:
				quit()
			else:
				exepath.pop(fc)
		file=open('data.txt','w')
		file.write(str(wall))
		file.close()
		if end==1:
			break

#move to neighbor point,test whether they are harder
		next=1
		while next>0:
			next=0
			for i in range (5):
				if i ==0:
					if move==0:
						continue
					else:
						testwall=addsub(x,y,curwall)
						repath,renodes,refringe=choose(order,testwall)
						if repath==[]:
							continue
						tsindex=(repath,renodes,refringe)
						if isHarder(curindex,tsindex,q):
							next=1
							del curwall
							curwall=testwall[:]
							del curindex
							a=tsindex[0]
							a1=a[:]
							b=tsindex[1]
							c=tsindex[2]
							curindex=(a1,b,c)
							nx=x
							ny=y

				if i==1:
					if test(x-1,y)==1:
						continue
					testwall=addsub(x-1,y,curwall)
					repath,renodes,refringe=choose(order,testwall)
					if repath==[]:
						continue
					tsindex=(repath,renodes,refringe)
					if isHarder(curindex,tsindex,q):
						next=1
						del curwall
						curwall=testwall[:]
						del curindex
						a=tsindex[0]
						a1=a[:]
						b=tsindex[1]
						c=tsindex[2]
						curindex=(a1,b,c)
						nx=x-1
						ny=y
						move=1
					
				if i==2:
					if test(x+1,y)==1:
						continue
					testwall=addsub(x+1,y,curwall)
					repath,renodes,refringe=choose(order,testwall)
					if repath==[]:
						continue
					tsindex=(repath,renodes,refringe)
					if isHarder(curindex,tsindex,q):
						next=1
						del curwall
						curwall=testwall[:]
						del curindex
						a=tsindex[0]
						a1=a[:]
						b=tsindex[1]
						c=tsindex[2]
						curindex=(a1,b,c)
						nx=x+1
						ny=y
						move=1
					
				if i==3:
					if test(x,y-1)==1:
						continue
					testwall=addsub(x,y-1,curwall)
					repath,renodes,refringe=choose(order,testwall)
					if repath==[]:
						continue
					tsindex=(repath,renodes,refringe)
					if isHarder(curindex,tsindex,q):
						next=1
						del curwall
						curwall=testwall[:]
						del curindex
						a=tsindex[0]
						a1=a[:]
						b=tsindex[1]
						c=tsindex[2]
						curindex=(a1,b,c)
						nx=x
						ny=y-1
						mvoe=1
					
				if i==4:
					if test(x,y+1)==1:
						continue
					testwall=addsub(x,y+1,curwall)
					repath,renodes,refringe=choose(order,testwall)
					if repath==[]:
						continue
					tsindex=(repath,renodes,refringe)
					if isHarder(curindex,tsindex,q):
						next=1
						del curwall
						curwall=testwall[:]
						del curindex
						a=tsindex[0]
						a1=a[:]
						b=tsindex[1]
						c=tsindex[2]
						curindex=(a1,b,c)
						nx=x
						ny=y+1
						move=1
			x=nx
			y=ny
		everyImprove=improve(orgindex,curindex,q)
		writeFile(order,everyImprove)
		if isHarder(maxindex,curindex,q):
			del maxwall
			maxwall=curwall[:]
			del maxindex
			d=curindex[0]
			d1=d[:]
			e=curindex[1]
			f=curindex[2]
			maxindex=(d1,e,f)
			print "success"
	
	writeFile(order,maxwall)
	order=raw_input("choose search algorithm('quit' to end):")
