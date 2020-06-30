# coding:utf-8

class Heap(object):
  def __init__(self, is_min=True):
    self.heap_array = []
    self.length = 0
    self.coef = 1 if is_min else -1
  
  def buildHeap(self, array):
    for n in array:
      self._add(n)
  
  def extractMin(self):
    if self.length == 0:
      raise IndexError
    min_num = self.heap_array[0]
    self._bubbleDown()
    return min_num
  
  def _add(self, item):
    self.heap_array.append(item)
    self.length += 1
    self._bubbleUp()
  
  def _bubbleUp(self):
    idx_last = self.length
    while self.heap_array[idx_last - 1] * self.coef < self.heap_array[idx_last // 2 - 1] * self.coef:
      if idx_last - 1 == 0:
        break
      self.heap_array[idx_last - 1], self.heap_array[idx_last // 2 - 1] = self.heap_array[idx_last // 2 - 1], self.heap_array[idx_last - 1]
      idx_last = idx_last // 2
  
  def _bubbleDown(self):
    last_item = self.heap_array.pop()
    self.length -= 1
    self.heap_array[0] = last_item
    idx_start = 1
    while idx_start * 2 + 1 <= self.length:
      min_child = idx_start * 2 - 1 \
        if self.heap_array[idx_start * 2 - 1] * self.coef < self.heap_array[idx_start * 2] * self.coef \
          else idx_start * 2
      if self.heap_array[idx_start - 1] * self.coef > self.heap_array[min_child] * self.coef:
        self.heap_array[idx_start - 1], self.heap_array[min_child] = self.heap_array[min_child], self.heap_array[idx_start - 1]
        idx_start = min_child + 1
      else:
        break
    
    if idx_start * 2 <= self.length:
      if self.heap_array[idx_start - 1] < self.heap_array[idx_start * 2 - 1]:
        self.heap_array[idx_start - 1], self.heap_array[idx_start * 2 - 1] = self.heap_array[idx_start - 1], self.heap_array[idx_start * 2 - 1]

if __name__ == '__main__':
  array = [11, 13, 4, 4, 8, 4, 12, 4, 9]
  heap = Heap()
  heap.buildHeap(array)
  print(heap.heap_array)
  try:
    while True:
      print(heap.extractMin())
  except IndexError:
    print('Finished.')
  

    
