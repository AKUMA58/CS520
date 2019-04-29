from sklearn.cluster import KMeans
import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

def readData(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        input_list = list(reader)
    for i in range(len(input_list)):
        for j in range(len(input_list[0])):
            input_list[i][j] = int(input_list[i][j])
    return input_list

def cluster(filename):
    data = readData(filename)
    X = []
    Y = []
    for i in range(10, 101, 1):
        kmeans = KMeans(n_clusters=i, random_state=0).fit(data)
        X.append(i)
        Y.append(kmeans.inertia_)
        print(filename,i,kmeans.inertia_)
    return X,Y

def data2csv(data, target):
    X,Y = data
    with open(target, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(X)
        writer.writerow(Y)

def data2plot(data, setting):
    X,Y = data
    fig, ax = plt.subplots()
    ax.plot(X, Y)

    ax.set(xlabel=setting['xlabel'], ylabel=setting['ylabel'],
           title=setting['title'])

    major_ticks = np.arange(0, 101, 5)
    ax.set_xticks(major_ticks)
    ax.grid()
    fig.savefig(setting['filename'])


def csv2plot(filename, setting):
    my_data = genfromtxt(filename, delimiter=',')
    data2plot(my_data,setting)




if __name__== "__main__":
    # if already get <k, error> data, we don't need to runRegression k-means, all we need to do is read data from dsv.
    ready = False

    if ready == False:
        # grey
        dataG = cluster('input.csv')
        data2csv(dataG, 'greyError.csv')

        # color
        dataC = cluster('color.csv')
        data2csv(dataC, 'colorError.csv')

    settingG = {"xlabel":"number of clusters", "ylabel":"error","title":"relationship of error and k in gray-scale clustering ","filename":"greyError.png"}
    csv2plot('greyError.csv',settingG)
    settingC = {"xlabel":"number of clusters k", "ylabel":"error","title":"relationship of error and k in color clustering","filename":"colorError.png"}
    csv2plot('colorError.csv',settingC)































