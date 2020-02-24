# coding:utf-8

class BinHeap(object):
  def __init__(self):
    self.heaplist = [0]
    self.currentSize = 0
    self.vertices = {}  # this is just for the Dijkstras_Algorithm

  def insert(self, x):
    if x[0] not in self.vertices:
      self.vertices[x[0]] = None
      self.heaplist.append(x)
      self.currentSize +=1
      self._percUp(self.currentSize)
    else:
      for i, (v, _) in enumerate(self.heaplist[1:]):
        i +=1
        if v == x[0]:
          self.heaplist[i] = x
          
  def _percUp(self, i):
    while i // 2 > 0:
      if self.heaplist[i][1] < self.heaplist[i // 2][1]:
        self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
      i = i // 2
  
  def delMin(self):
    retval = self.heaplist[1]
    self.heaplist[1] = self.heaplist[self.currentSize]
    self.currentSize -=1
    self.heaplist.pop()
    self._perDown(1)
    return retval
  
  def _perDown(self, i):
    while i * 2 <= self.currentSize:
      mi = self._minChild(i)
      if self.heaplist[i][1] > self.heaplist[mi][1]:
        self.heaplist[i], self.heaplist[mi] = self.heaplist[mi], self.heaplist[i]
      i = mi
  
  def _minChild(self, i):
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
      if self.heaplist[i * 2][1] < self.heaplist[i * 2 + 1][1]:
        return i * 2
      else:
        return i * 2 + 1

  def buildHeap(self, array):
    i = len(array) // 2
    self.currentSize = len(array)
    self.heaplist = [0] + array
    while i > 0:
      self._perDown(i)
      i -=1