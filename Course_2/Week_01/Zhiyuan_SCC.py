import numpy as np
import copy
import random

class Vertex:
    def __init__(self):
        self.visited = False
        self.leader = -1
        self.outEdge = []

class MyStack:
    def __init__(self,origin):
        self.container = [origin]
        self.count = 1
    def show(self):
        print(self.container)
    def push(self,element):
        self.count += 1
        self.container.append(element)
    def pop(self):
        if self.count > 0:
            self.count -= 1
            del self.container[self.count]
    def get(self):
        if self.count == 0:
            return False
        else:
            return self.container[self.count-1]
        
class MyQuickSort:
    def MySwap(self,MyArray,appendix,i,j):
        temp = MyArray[i]
        MyArray[i] = MyArray[j]
        MyArray[j] = temp
        temp = appendix[i]
        appendix[i] = appendix[j]
        appendix[j] = temp
    def Sort(self,MyArray,appendix,left,right):
        if left == right:
            return
        random.seed()
        pivot = random.randint(left,right)
        self.MySwap(MyArray,appendix,left,pivot)
        i = left+1 # first element in the right  
        j = left+1 # last element in the right +1
        while j <= right:
            if MyArray[j] > MyArray[left]:
                self.MySwap(MyArray,appendix,i,j)
                i += 1
            j += 1
        self.MySwap(MyArray,appendix,left,i-1)
        if i > left+2:
            self.Sort(MyArray,appendix,left,i-2)
        if right > i:
            self.Sort(MyArray,appendix,i,right)

def readData(filename,n):
    vertexArray = [Vertex() for i in range(n)]
    vertexArrayR = [Vertex() for i in range(n)]
    file = open(filename)
    InputData = file.readlines()
    for i in InputData:
        temp = list(map(int,i.split(' ')[:-1]))
        vertexArray[temp[0]-1].outEdge.append(temp[1]-1)
        vertexArrayR[temp[1]-1].outEdge.append(temp[0]-1)
    return vertexArray,vertexArrayR
    
def DFS(vertexArray,origin,orders): # assume origin is not visited yet
    s = MyStack(origin)
    count = 0 # count the number of vertex in current SCC
    while s.count > 0:
        # s.show()
        index = s.get()
        if vertexArray[index].visited: # if already visited, go back
            if vertexArray[index].leader == -1:
                vertexArray[index].leader = origin # if index == origin it completes a circle
                orders.append(index)
                count += 1
            s.pop()
        else: # if not visited yet, go forward
            vertexArray[index].visited = True
            for i in vertexArray[index].outEdge:
                if vertexArray[i].visited == False:
                    s.push(i)
    return count
    
if __name__ == "__main__":
    n = 875714
    filename = 'SCC.txt'
    # n = 11
    # filename = 'SCCDemo.txt'
    print("reading file")
    vertexArray,vertexArrayR = readData(filename,n)
    ordersR = []
    print("1st DFS")
    for i in range(n):
        if vertexArrayR[i].visited == False:
            DFS(vertexArrayR,i,ordersR)
    SCCs = []
    SCCVertexCount = []
    print("2nd DFS")
    for i in range(n-1,-1,-1):
        if vertexArray[ordersR[i]].visited == False:
            orders = []
            SCCVertexCount.append(DFS(vertexArray,ordersR[i],orders))
            SCCs.append(copy.deepcopy(orders))
    print("Sorting")
    MQS = MyQuickSort()
    MQS.Sort(SCCVertexCount,SCCs,0,len(SCCs)-1)
    