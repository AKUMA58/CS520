from random import random

class Map:

    def __init__(self):
        self.n = 50
        self.map = self.generateMap()
        self.fn = dict()
        self.target = None
        self.init()


    def init(self):
        self.fn['flat'] = 0.1
        self.fn['hilly'] = 0.3
        self.fn['forested'] = 0.7
        self.fn['cave'] = 0.9
        rx = int(self.n*random())
        ry = int(self.n*random())
        self.target = rx,ry


    def generateMap(self):
        map = dict()
        for i in range(self.n):
            for j in range(self.n):
                map[(i,j)] = dict()
                map[(i,j)]['neighbours'] = set()
        for i in range(self.n):
            for j in range(self.n):
                neiSet = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
                for (nx,ny) in neiSet:
                    if nx >= 0 and nx < self.n and ny >= 0 and ny < self.n:
                        map[(i, j)]['neighbours'].add((nx,ny))
                # map[(i,j)]['P_cost']=0.0
                map[(i,j)]['p'] = 1
                p = random()
                if p < 0.2:
                    map[(i,j)]['type'] = 'flat'
                elif p < 0.5:
                    map[(i,j)]['type'] = 'hilly'
                elif p < 0.8:
                    map[(i,j)]['type'] = 'forested'
                else:
                    map[(i,j)]['type'] = 'cave'
        return map