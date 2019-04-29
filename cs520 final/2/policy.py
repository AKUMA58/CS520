replacecost=250
b=0.8
state=[100,90,80,70,60,50,40,30,20,10]
for i in range (2000):
	tsstate=[]
	policy=[]
	tsstate.append(100+b*(1*state[1]))
	policy.append(1)
	for j in range (1,9):
		tsstate.append(max(100-10*j+b*((1-0.1*j)*state[j]+0.1*j*state[j+1]),-replacecost+b*state[0]))
		if max(100-10*j+b*((1-0.1*j)*state[j]+0.1*j*state[j+1]),-replacecost+b*state[0])==-replacecost+b*state[0]:
			policy.append(0)
		else:
			policy.append(1)
	tsstate.append(-replacecost+b*state[0])
	policy.append(0)
	state=tsstate
for i in range (251):
	if (float(i)/float(250)*state[0])>0.5*(state[1]+state[2]):
		count=i-1
		break
print count
print state
print policy