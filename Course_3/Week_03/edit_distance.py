# coding:utf-8

def calculateDistance(str_a, str_b):
  length_a = len(str_a)
  length_b = len(str_b)

  distance = [[0 for _ in range(length_b+1)] for _ in range(length_a+1)]
  batchtrace = [[None for _ in range(length_b+1)] for _ in range(length_a+1)]

  for i in range(length_a+1):
    for j in range(length_b+1):
      if i == 0:
        distance[i][j] = j
      elif j == 0:
        distance[i][j] = i
      else:
        if str_a[i-1] == str_b[j-1]:
          distance[i][j] = distance[i-1][j-1]
          batchtrace[i][j] = ((i-1, j-1), 'no action')
        else:
          insert_dist = distance[i][j-1]
          delete_dist = distance[i-1][j]
          replace_dist = distance[i-1][j-1]
          dist_cands = [insert_dist, delete_dist, replace_dist]
          choose_dist = min(dist_cands) 
          select = dist_cands.index(choose_dist)
          distance[i][j] = choose_dist + 1
          if select == 0:
            batchtrace[i][j] = ((i, j-1), 'insert {}'.format(str_b[j-1]))
          elif select == 1:
            batchtrace[i][j] = ((i-1, j), 'delete {}'.format(str_a[i-1]))
          else:
            batchtrace[i][j] = ((i-1, j-1), 'replace {}{}'.format(str_a[i-1], str_b[j-1]))
  
  p_prev = batchtrace[-1][-1]
  path = []
  while p_prev is not None:
    path.append(p_prev[1])
    i, j = p_prev[0][0], p_prev[0][1]
    p_prev = batchtrace[i][j]

  return distance[-1][-1], list(reversed(path))

if __name__ == '__main__':
  dist, batchtrace = calculateDistance('ABC', 'ACD')
  print(dist)
  print(batchtrace)