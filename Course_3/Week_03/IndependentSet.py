# coding:utf-8

def main(array):
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

if __name__ == '__main__':
  array = [3, 6, 2, 1, 11]
  res, backtrace = main(array)
  print(res)
  print(backtrace)