# coding:utf-8

import codecs
from collections import defaultdict

class Vertex(object):
	def __init__(self, value):
		self.value = value
	
	def __eq__(self, other):
		return self.value == other.value
	
	def __str__(self):
		return str(self.value)
	
	def __hash__(self):
		return hash(self.value)

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self, u, v):
		self.graph[u].append(v)
		if v not in self.graph.keys():
			self.graph[v] = []
	
	def DFSInner(self, s, explored_list):
		self.result.append(s)
		explored_list[s] = True

		for ver in self.graph[s]:
			if not explored_list[ver]:
				self.DFSInner(ver, explored_list)

	def DFS(self, s):
		explored_list = {}
		for ver in self.graph.keys():
			explored_list[ver] = False
		self.result = []

		self.DFSInner(s, explored_list)
		if not all(explored_list.values()):
			for ver, val in explored_list.items():
				if not val:
					self.DFSInner(ver, explored_list)
		return self.result
	
	def topologicalSort_inner(self, ver, explored_list):
		explored_list[ver] = True

		for u in self.graph[ver]:
			if not explored_list[u]:
				self.topologicalSort_inner(u, explored_list)
		
		self.result_topo.append(ver)

	def topologicalSort(self):
		explored_list = {}
		start_vertex = []
		for ver in self.graph.keys():
			explored_list[ver] = False
			if len(self.graph[ver]) == 0:
				start_vertex.append(ver)
		self.result_topo = []

		for ver in start_vertex:
			if not explored_list[ver]:
				self.topologicalSort_inner(ver, explored_list)

		for ver in self.graph.keys():
			if not explored_list[ver]:
				self.topologicalSort_inner(ver, explored_list)
		
		return reversed(self.result_topo)

	def DFS_BY_STACK(self, s):
		explored_list = {}
		for ver in self.graph.keys():
			explored_list[ver] = False
		self.result = []
		stack = [s]

		result = [s]
		current_vertex = s
		while len(stack) != 0:
			if len(self.graph[current_vertex]) == 0:
				break
			for ver in self.graph[current_vertex]:
				if not explored_list[ver]:
					explored_list[ver] = True
					result.append(ver)
					stack.append(ver)
					current_vertex = ver
				else:
					stack.pop(-1)
		return result

def readGraph(path):
	split_tag = '\t' if path == 'kargerMinCut.txt' else ' '
	graph = Graph()
	with codecs.open(path, 'r', 'utf-8') as file:
		for line in file:
			line = line.strip().split(split_tag)
			v1 = Vertex(int(line[0]))
			others = list(map(int, line[1:]))
			for o in others:
				graph.addEdge(v1, Vertex(o))
	return graph

if __name__ == '__main__':
	# build the graph, 'test_graph.txt' for testing 'Undirected Connectivity'
	graph = readGraph('test_graph_for_2.txt')

	# # DFS
	# start_v = list(graph.graph.keys())[5]
	# for k in list(graph.graph.keys()):
	# 	print(k)
	# result = graph.DFS(start_v)
	# print('The Graph contains {} vertexs.'.format(len(result)))
	# for v in result:
	# 	print(v)

	# topological sort
	result_topo = graph.topologicalSort()
	print()
	for v in result_topo:
		print(v)