# coding:utf-8

import codecs
from collections import defaultdict

class Vertex(object):
  def __init__(self, name):
    self.name = name
  
  def __eq__(self, other):
    return self.name == other.name
  
  def __str__(self):
    return self.name
  
  def __hash__(self):
    return hash(self.name)

class DIJKSTRA_ALGORITHM(object):
  X = []  # node processed so far
  A = {}  # the shortest distance for the node in x so far
  B = {}  # the previous node for the node in x so far

  @classmethod
  def find_sp(cls, graph, s, e):
    cls.X.append(s)
    cls.A[s] = 0
    cls.B[s] = None

    for v in cls.X: # tail founded
      if e not in cls.A.keys(): # the end node 'e' has not been found
        min_dist = 100000
        for tail_part in graph[v]:
          tail, dist = tail_part[0], tail_part[1]
          if dist < min_dist:
            candidate = tail
            min_dist = dist
        cls.X.append(candidate)
        cls.A[candidate] = cls.A[v] + min_dist
        cls.B[candidate] = v
      else:
        path =cls.find_path(e)
        return cls.A[e], path
  
  @classmethod
  def find_path(cls, e):
    path = []
    cur_node = e
    while True:
      prev = cls.B[cur_node]
      if prev is not None:
        path.append(prev)
        cur_node = prev
      else:
        break
    return reversed(path)

def build_graph(path):
  graph = defaultdict(list)

  with codecs.open(path, 'r', 'utf-8') as file:
    for line in file:
      line_split = line.strip().split(' ')
      head = Vertex(line_split[0])
      tails = line_split[1:]
      
      for tail in tails:
        v, d = tail.split('|')
        graph[head].append((Vertex(v), float(d)))

  return graph

if __name__ == '__main__':
  graph = build_graph('dijkstras_graph_text.txt')
  
  distance, path = DIJKSTRA_ALGORITHM().find_sp(graph, Vertex('s'), Vertex('t'))
  print(distance)
  for v in path:
    print(v)