import numpy as np
import re
import itertools


def getTrainData(classA_path, classB_path):
    x_train_list = list()
    y_train_list = list()
    train_pattern = list()

    fa = open(classA_path)
    for line in fa:
        #print(line)
        if len(line)==5:
            continue
        else:
            line_pattern = re.split('\t', line[0:9])
            line_pattern = [int(x) for x in line_pattern]
            train_pattern.append(line_pattern)
            if len(train_pattern) == 5:
                x_train_list.append(list(itertools.chain.from_iterable(train_pattern)))
                y_train_list.append(0)
                train_pattern = list()

    fb = open(classB_path)
    for line in fb:
        #print(line)
        if len(line)==5:
            continue
        else:
            line_pattern = re.split('\t', line[0:9])
            line_pattern = [int(x) for x in line_pattern]
            train_pattern.append(line_pattern)
            if len(train_pattern) == 5:
                x_train_list.append(list(itertools.chain.from_iterable(train_pattern)))
                y_train_list.append(1)
                train_pattern = list()


    x_train = np.array(x_train_list)
    y_train = np.array(y_train_list)

    return (x_train, y_train)

def getTestData(mystery_path):
    x_test_list = list()
    train_pattern = list()
    f = open(mystery_path)
    for line in f:
        #print(line)
        if len(line)==5:
            continue
        else:
            line_pattern = re.split('\t', line[0:9])
            line_pattern = [int(x) for x in line_pattern]
            train_pattern.append(line_pattern)
            if len(train_pattern) == 5:
                x_test_list.append(list(itertools.chain.from_iterable(train_pattern)))
                train_pattern = list()
    x_test = np.array(x_test_list)
    return x_test


def knnpredict(x_train, y_train, x_test,k):
	result=[]
	for test in x_test:
		dists=dict()
		compare=[]
		for i in range (len(x_train)):
			dis=np.linalg.norm(x_train[i]-test)
			dists[dis]=y_train[i]
		sort=sorted(dists)
		for j in range (k):
			compare.append(dists[sort[j]])
		countA=0
		countB=0
		for i in range (len(compare)):	
			if compare[i]==0:
				countA+=1
			if compare[i]==1:
				countB+=1
		if countA>countB:
			result.append(0)
		else:
			result.append(1)
	return result



def naive_bayes_predict(x_train, y_train,x_test):
    x=[]
    y=[]
    px=[]
    py=[]
    result=[]
    for i in range (len(x_train)):
    	if y_train[i]==0:
    		x.append(x_train[i])
    	else:
    		y.append(x_train[i])
    for i in range (len(x[0])):
    	count=0
    	for j in range (len(x)):
    		if x[j][i]==1:
    			count+=1
    	px.append(float(count+1)/float(len(x)+2))
    for i in range (len(y[0])):
    	count=0
    	for j in range (len(y)):
    		if y[j][i]==1:
    			count+=1
    	py.append(float(count+1)/float(len(y)+2))
    for test in x_test:
    	resultx=0.5
    	resulty=0.5
    	for i in range(len(test)):
    		if test[i]==1:
    			resultx=resultx*px[i]
    			resulty=resulty*py[i]
    		else:
	    		resultx=resultx*(1-px[i])
    			resulty=resulty*(1-py[i])
    	if resultx>resulty:
    		result.append(0)
    	else:
    		result.append(1)
    return result


(x_train, y_train) = getTrainData('ClassA.txt', 'ClassB.txt')
x_test = getTestData('Mystery.txt')
knnresult=knnpredict(x_train, y_train, x_test,3)
print "KNN result:",knnresult
bayesresult=naive_bayes_predict(x_train, y_train,x_test)
print "naive_bayes result:",bayesresult

