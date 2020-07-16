# coding:utf-8

def findSolution(items, weight):
  values = [[0 for _ in range(weight+1)] for _ in range(len(items)+1)]
  batcktrace = [[None for _ in range(weight+1)] for _ in range(len(items)+1)]

  for i in range(1, len(items)+1):
    for x in range(weight+1):
      v, w = items[i-1][0], items[i-1][1]
      cand_a = values[i-1][x]
      if w > x:
        cand_b = cand_a
      else:
        cand_b = values[i-1][x-w] + v
      if cand_a > cand_b:
        values[i][x] = cand_a
        batcktrace[i][x] = (i-2, i-2)
      else:
        values[i][x] = cand_b
        batcktrace[i][x] = (i-2, i-1)
        
  p_prev = batcktrace[-1][-1]
  path = []
  while p_prev[0] != 0:
    row, col = p_prev[0], p_prev[1]
    if row == col:
      path.append(row)
    else:
      path.append(col)
      path.append(row)
    p_prev = batcktrace[row][col]

  return values[-1][-1], path

if __name__ == '__main__':
  weight = 6
  items = [(3,4), (2,3), (4,2), (4,3)]
  value, path = findSolution(items, weight)
  print(value)
  print(path)