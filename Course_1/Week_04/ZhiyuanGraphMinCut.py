import numpy as np
import random
import sys
import copy

def findVertexGroup(vertex,index):
    if vertex[index] != index:
        path = [index]
        index = vertex[index]
        while vertex[index] != index:
            path.append(index)
            index = vertex[index]
        for i in path:
            vertex[i] = index
    return index

def findMinCut(vertex,edge):
    nVertex = len(vertex)
    nEdge = len(edge)
    while nVertex >2:
        indexEdge = random.randint(0,nEdge-1)
        indexVertex1 = findVertexGroup(vertex,edge[indexEdge][0])
        indexVertex2 = findVertexGroup(vertex,edge[indexEdge][1])
        if indexVertex1 != indexVertex2:
            vertex[indexVertex2] = vertex[indexVertex1]
            nVertex -= 1
        del edge[indexEdge]
        nEdge -= 1
    i = nEdge-1
    while i>=0:
        indexVertex1 = findVertexGroup(vertex,edge[i][0])
        indexVertex2 = findVertexGroup(vertex,edge[i][1])
        if indexVertex1 == indexVertex2:
            del edge[i]
            nEdge -= 1
        i -= 1
    return vertex,nEdge

if __name__ == "__main__":
    filename = "kargerMinCut.txt"
    file = open(filename)
    InputData = file.readlines()
    graph = []
    for i in InputData:
        graph.append(list(map(int,i.split('\t')[:-1])))
    n = len(graph)
    vertex = np.array(range(n)) # all the vertex is reduced by 1 
    edge = []
    for i in range(n):
        if len(graph[i])==1:
            print("vertex %s is isolated" %i)
            sys.exit(0)
        else:
            for j in range(1,len(graph[i])):
                if graph[i][0] < graph[i][j]: # avoid identical edges
                    edge.append([graph[i][0]-1,graph[i][j]-1])
    iterations = n**2
    minCut = len(graph[0])
    minCutHistory = []
    minCutVertex = 0
    random.seed()
    for i in range(iterations):
        print ("processing %ith iteration" %i)
        newVertex,newMinCut = findMinCut(copy.deepcopy(vertex),copy.deepcopy(edge))
        minCutHistory.append(newMinCut)
        if newMinCut < minCut:
            minCutVertex = newVertex
            minCut = newMinCut
            
    
        