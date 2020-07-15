# coding:utf-8

import time
import random

def dpSolve(array):
  cache = []
  cache.append(array[0])
  cache.append(array[1])
  length = len(array)

  for i in range(2, len(array)):
    cache.append(max(cache[i-1], cache[i-2] + array[i]))
  
  backtrace = []
  i = length - 1
  while i >= 1:
    if cache[i-1] >= cache[i-2] + array[i]:
      i -=1
    else:
      backtrace.append(i)
      i -= 2

  return cache[length - 1], list(reversed(backtrace))

def naiveSolve(array):
  if len(array) == 1:
    return array[0]
  elif len(array) == 2:
    return max(array[0], array[1])
  else:
    return max(naiveSolve(array[:-1]), naiveSolve(array[:-2]) + array[-1])

if __name__ == '__main__':
  array = [random.randint(0, 10000) for _ in range(35)]
  time_s = time.time()
  print(naiveSolve(array))
  time_e = time.time()
  print('Naive method costs: {}s.'.format(time_e - time_s))

  time_s = time.time()
  res, backtrace = dpSolve(array)
  print(res)
  print(backtrace)
  time_e = time.time()
  print('Dynamic Programming costs: {}s'.format(time_e - time_s))