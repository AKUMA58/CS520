import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import linear_model
import png
from numpy import genfromtxt
from collections import Counter
from visualize import data2pngColor, data2pngGrey
from itertools import combinations_with_replacement

def readData(filename):
    data = genfromtxt(filename, delimiter=',')
    return data


def cluster(data, k):
    km = KMeans(n_clusters=k, random_state=0).fit(data)
    return km


def createTrainingData(data1, data2, k1, k2):
    data = dict()
    km1 = cluster(data1, k1)
    km2 = cluster(data2, k2)
    for i in range(len(data1)):
        # grey point
        g = data1[i]
        indexG = km1.predict([g])[0]
        # grey center
        gc = km1.cluster_centers_[indexG]
        # color point
        c = data2[i]
        indexC = km2.predict([c])[0]
        # color center
        cc = km2.cluster_centers_[indexC]
        if tuple(gc) not in data:
            data[tuple(gc)] = []
        data[tuple(gc)].append(tuple(cc))
    X = []
    Y = []
    for key in data:
        top = Counter(data[key]).most_common(1)[0][0]
        key=list(key)
        for x in combinations_with_replacement(range(9),2):
            temp=key[x[0]]*key[x[1]]
            key.append(temp)
            print(temp)
        X.append(list(key))
        Y.append(list(top))
    return X,Y,km1
        


def color2ind(Y):
    ind_map = {}
    color = []
    for item in Y:
        color.append(tuple(item))
    color = set(color)
    i = 0
    for each_col in color:
        ind_map[each_col] = i
        i += 1
    return ind_map

def nn(X, Y):
    # clf = LogisticRegression()
    #clf = linear_model.SGDClassifier()
    clf = SVC()
    #clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(30, 10), random_state=1)
    X = np.array(X)
    Y = np.array(Y)
    clf.fit(X, Y)
    return clf

def processdata(data,dtcluster):
    data_cluster=[]
    for i in range(len(data)):
        # grey point
        g = data[i]
        indexG = dtcluster.predict([g])[0]
        # grey center
        gc = dtcluster.cluster_centers_[indexG]
        gc=list(gc)
        # print gc
        #combination
        for x in combinations_with_replacement(range(9),2):
            temp=gc[x[0]]*gc[x[1]]
            gc.append(temp)
        data_cluster.append(list(gc))
    # print data_cluster
    return data_cluster


def run():
    data = readData('input.csv')
    # print data
    data1 = readData('palmGrey.csv')
    data2 = readData('palmColor.csv')
    k1 = 40
    k2 = 35
    # km1 = cluster(data1, k1)
    X,Y,greycluster = createTrainingData(data1, data2, k1, k2)
    inputdata=processdata(data,greycluster)
    map_index = color2ind(Y)
    clf_Y = []
    for item in Y:
        clf_Y.append(map_index[tuple(item)])
    #clf = nn(X, Y)
    clf = nn(X, clf_Y)
    color = []
    for g in inputdata:
        rc = clf.predict([g])[0]
        clf_rc = list(map_index.keys())[list(map_index.values()).index(rc)]
        #color.append(rc)
        color.append(clf_rc)
    outputdata = []
    for i in color:
        temp = []
        for j in i:
            # avoid overflowing
            if j > 255:
                j = 255
            if j < 0:
                j = 0
            temp.append(int(j))
        outputdata.append(temp)
    # print(outputdata)
    data2pngColor(outputdata, 281, 'trainFromPalmOutputPalmColor.png')


def output(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in data:
            print(row)
            spamwriter.writerow(row)



run()
