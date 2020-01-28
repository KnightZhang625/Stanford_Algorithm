import numpy as np
import random
import sys
import copy

def mergeVertex(vertex,index1,index2):
    for i in range(len(vertex)):
        if vertex[i] == index2:
            vertex[i] = index1

def findMinCut(vertex,edge):
    nVertex = len(vertex)
    nEdge = len(edge)
    while nVertex >2:
        indexSel = random.randint(0,nEdge-1)
        # print("nEdge=%i" %nEdge)
        # print("nVertex=%i" %nVertex)
        if vertex[edge[indexSel][0]-1] != vertex[edge[indexSel][1]-1]:
            mergeVertex(vertex,vertex[edge[indexSel][0]-1],vertex[edge[indexSel][1]-1])
            nVertex -= 1
        del edge[indexSel]
        nEdge -= 1
    i = nEdge-1
    while i>=0:
        if vertex[edge[i][0]-1] == vertex[edge[i][1]-1]:
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
    vertex = np.array(range(1,n+1)) 
    edge = []
    for i in range(n):
        if len(graph[i])==1:
            print("vertex %s is isolated" %i)
            sys.exit(0)
        else:
            for j in range(1,len(graph[i])):
                if graph[i][0] < graph[i][j]: # avoid identical edges
                    edge.append([graph[i][0],graph[i][j]])
    iterations = n**1
    minCut = len(graph[0])
    minCutHistory = []
    minCutVertex = 1
    random.seed()
    for i in range(iterations):
        print ("processing %ith iteration" %i)
        newVertex,newMinCut = findMinCut(copy.deepcopy(vertex),copy.deepcopy(edge))
        minCutHistory.append(newMinCut)
        if newMinCut < minCut:
            minCutVertex = newVertex
            minCut = newMinCut
            
    
        