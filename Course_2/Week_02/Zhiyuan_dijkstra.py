class Edge:
    def __init__(self,inputList):
        self.destination = inputList[0]-1
        self.length = inputList[1]

class Vertex:
    def __init__(self,inputString):
        self.edges = []
        for i in inputString.split('\t')[1:-1]:
            self.edges.append(Edge(list(map(int,i.split(',')))))
        self.processed = False
        
class MyHeap:
    def __init__(self,n): #vertex,n):
        self.positions = [-1 for i in range(n)] # keeps track of vertex positions in the heap
        self.count = 0
        self.index = []
        self.dist = []
        self.path = []
    
    def display(self):
        print(self.dist)
            
    def swap(self,i,j):
        temp = self.index[i],self.dist[i],self.path[i]
        self.index[i],self.dist[i],self.path[i] = self.index[j],self.dist[j],self.path[j]
        self.index[j],self.dist[j],self.path[j] = temp
        self.positions[self.index[i]] = i
        self.positions[self.index[j]] = j
        
    def insert(self,index,dist,path):
        self.count += 1
        self.index.append(index)
        self.dist.append(dist)
        self.path.append(path)
        self.positions[index] = self.count-1
        i = self.count-1 # current node
        j = self.count//2-1 # parent node
        while j >= 0 and self.dist[i] < self.dist[j]:
            self.swap(i,j)
            i = j
            j = (i+1)//2-1
            
    def pop(self):
        if self.count == 0:
            return False
        output = self.index[0],self.dist[0],self.path[0]
        self.count -= 1
        self.positions[self.index[0]] = -1 # clear this position
        self.index[0],self.dist[0],self.path[0] = self.index[self.count],self.dist[self.count],self.path[self.count]
        del(self.index[self.count])
        del(self.dist[self.count])
        del(self.path[self.count])
        i = 0 # parent
        j1 = 1 # left child
        j2 = 2 # right child
        while j2 < self.count: # right child exist
            if self.dist[i]>self.dist[j1] or self.dist[i]>self.dist[j2]:
                if self.dist[j1] < self.dist[j2]:
                    self.swap(i,j1)
                    i = j1
                else:
                    self.swap(i,j2)
                    i = j2
                j1 = 2*i+1
                j2 = 2*i+2
            else:
                break
        if j1<self.count and self.dist[i]>self.dist[j1]: # check left child
            self.swap(i,j1)
        return output
    
    def update(self,index,dist,path): # update index that already exist, or insert index that does not exist
        if self.positions[index] == -1: # not in the heap
            self.insert(index,dist,path)
        else: # already in the heap
            i = self.positions[index]
            if dist < self.dist[i]: # update only if new dist is smaller
                self.dist[i] = dist
                self.path[i] = path
                j = (i+1)//2-1
                while j >= 0 and self.dist[i] < self.dist[j]:
                    self.swap(i,j)
                    i = j
                    j = (i+1)//2-1

def readData(filename):
    file = open(filename)
    InputData = file.readlines()
    vertexArray = []
    for s in InputData:
        vertexArray.append(Vertex(s))
    return vertexArray

def Dijkstra(vertexArray,sPath,sDist):
    n = len(vertexArray)
    sPath[0] = [0]
    sDist[0] = 0
    vertexArray[0].processed = True
    h = MyHeap(n)
    # frontier already marked in heap using self.positions
    i = 0 # index of the most recently added vertex
    for k in range(n-1):
        print("k=%i"%k)
        for e in vertexArray[i].edges:
            if vertexArray[e.destination].processed == False:
                h.update(e.destination,sDist[i]+e.length,sPath[i]+[e.destination])
        i,sDist[i],sPath[i] = h.pop()
        vertexArray[i].processed = True

if __name__ == "__main__":
    filename = "dijkstraData.txt"
    vertexArray = readData(filename)
    n = len(vertexArray)
    shortestPath = [[] for i in range(n)]
    shortestDist = [-1 for i in range(n)]
    Dijkstra(vertexArray,shortestPath,shortestDist)
    '''
    # following code is used to test heap
    temp = [8,6,3,1,5,2,4,7]
    mh = MyHeap(8)
    for i in range(8):
        mh.insert(i,temp[i],[])
        print(mh.dist)
    '''
    