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
		#vital part, this will make the vertex be the only one.
	 return hash(self.value)

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def BFS(self, s, return_dict=False):
		# initialize
		explored_list = {}
		for ver in self.graph.keys():
			explored_list[ver] = False
		explored_list[s] = True
		queue = [s]

		result = []
		while len(queue) != 0:
			v = queue.pop(0)
			result.append(v)
			for e in self.graph[v]:
				if not explored_list[e]:
					explored_list[e] = True
					queue.append(e)
		
		if return_dict:
			return result, explored_list
		else:
			return result

	def shortest_path(self, start, end):
		if start == end:
			return 0

		# initialize
		explored_list = {}
		distance_list = {}
		for ver in self.graph.keys():
			explored_list[ver] = False
			distance_list[ver] = 0
		explored_list[start] = True
		queue = [start]

		pre_vertex = {}		# save the pre-vertex of each vertex
		while len(queue) != 0:
			v = queue.pop(0)
			for e in self.graph[v]:
				if not explored_list[e]:
					explored_list[e] = True
					distance_list[e] = distance_list[v] + 1
					pre_vertex[e] = v
					if e == end:
						break
					queue.append(e)

		path = self._reverse_path(pre_vertex, end)
		return distance_list[end], path
	
	def _reverse_path(self, pre_vertex, end):
		path = []
		while True:
			try:
				pre_ = pre_vertex[end]
				path.append(pre_)
				end = pre_
			except KeyError:
				break
		return reversed(path)

	def find_connect(self):
		explored_list = {}
		for ver in self.graph.keys():
			explored_list[ver] = False
		
		clusters = []
		for ver in self.graph.keys():
			if not explored_list[ver]:
				components, updated_explored_list = self.BFS(ver, True)
				explored_list.update(updated_explored_list)
				clusters.append(components)

		return clusters

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
	graph = readGraph('kargerMinCut.txt')

	# BFS
	start_v = list(graph.graph.keys())[0]
	result = graph.BFS(start_v)
	print('The Graph contains {} vertexs.'.format(len(result)))

	# find shortest path between given vertexs
	start = Vertex(3)
	end = Vertex(7)
	shortest_distance, path = graph.shortest_path(start, end)
	print('The minimum distance from {} to {} is: {}'.format(start, end, shortest_distance))
	print('The path is: {}'.format([str(p) for p in path]))

	# find connected components
	clusters = graph.find_connect()
	for i, clu in enumerate(clusters):
		print('The {} cluster is: {}'.format(i, [str(c) for c in clu]))