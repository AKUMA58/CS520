tsmaze=[]
f=open("Localization.txt")
for line in f:
	tsmaze.append(line)
f.close()

#write maze
maze=[[0 for j in range(len(tsmaze[0])/2)] for i in range (len(tsmaze))]
for i in range (len(tsmaze)):
	for j in range (len(tsmaze[0])/2):
		maze[i][j]=tsmaze[i][2*j]

#find blank cells
blank=[]
for i in range (len(maze)):
	for j in range (len(maze[0])):
		if maze[i][j]=='0':
			blank.append((i,j))

#count block neighbor of blank cells
num_neighbor=dict()
for i in range (len(blank)):
	cell=blank[i]
	count=0
	for j in range (-1,2):
		for k in range (-1,2):
			if maze[cell[0]+j][cell[1]+k]=='1':
				count+=1
	num_neighbor[cell]=count

#move function
def move(direction,cell):
	if direction=='L':
		i=0
		j=-1
	if direction=='R':
		i=0
		j=1
	if direction=='U':
		i=-1
		j=0
	if direction=='D':
		i=1
		j=0
	if maze[cell[0]+i][cell[1]+j]=='0':
		cell=(cell[0]+i,cell[1]+j)
	return cell

#function of guess cell
def guess(observations,actions):
	cells=[]
	for i in range (len(blank)):
		if num_neighbor[blank[i]]==int(observations[0]):
			cells.append(blank[i])
	for i in range (len(actions)):
		for j in range (len(cells)):
			tscell=cells[0]
			cells.pop(0)
			tscell=move(actions[i],tscell)
			if num_neighbor[tscell]==int(observations[i+1]):
				cells.append(tscell)
	return cells

guesscells=guess('555','LL')
print guesscells
f=open('result.txt','w')
for i in range (len(guesscells)):
	f.write (str(guesscells[i]))
	f.write(' or ')
f.close()

print len(guesscells)
count_times=[]
for i in guesscells:
	count_times.append(guesscells.count(i))
print (guesscells[count_times.index(max(count_times))])
