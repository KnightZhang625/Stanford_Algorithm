# coding:utf-8

import copy
import codecs
import random

def buildGraph(path):
	vertics = []
	edges = []
	with codecs.open(path, 'r', 'utf-8') as file:
		for line in file:
			line = line.strip().split('\t')
			node = int(line[0])
			others = line[1: ]

			vertics.append(node)
			for o in others:
				o = int(o)
				if (node, o) not in edges:
					edges.append([node, o])
	return vertics, edges

def minimumCut(vertics, edges):
	while len(vertics) > 2:
		random.shuffle(edges)
		idx = random.choice(range(len(edges)))
		[u, v] = edges.pop(idx)
		vertics.remove(v)

		updated_edges = []
		for i, e in enumerate(edges):
			if e[0] == v:
				edges[i][0] = u
			elif e[1] == v:
				edges[i][1] = u

			if edges[i][0] != edges[i][1]:
				updated_edges.append(edges[i])

		edges = updated_edges

	return len(edges)

if __name__ == '__main__':
	vertics, edges = buildGraph('kargerMinCut.txt')

	for _ in range(40000):
		v = copy.deepcopy(vertics)
		e = copy.deepcopy(edges)
		print(minimumCut(v, e))



