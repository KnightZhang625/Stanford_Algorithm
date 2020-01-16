# coding:utf-8

import time
import codecs
import random

def build_graph(path):
	graph = {}
	with codecs.open(path) as file:
		for line in file:
			line = line.strip().split('\t')
			node = int(line[0])
			others = list(map(int, line[1:]))

			graph[node] = others

	return graph

def contract(graph, v, w):
	for node in graph[w]:
		if node != v:
			graph[v].append(node)
		graph[node].remove(w)
		if node != v:
			graph[node].append(v)
	del graph[w]

def kargerCut(graph):
	while len(graph) > 2:
		v = random.choice(list(graph.keys()))
		w = random.choice(graph[v])
		contract(graph, v, w)
	mincut = len(graph[list(graph.keys())[0]])
	return mincut

if __name__ == '__main__':
	time_s = time.time()
	for _ in range(40000):
		graph = build_graph('kargerMinCut.txt')
		mincut = kargerCut(graph)
		print(mincut)
	time_e = time.time()
	print(time_e - time_s)