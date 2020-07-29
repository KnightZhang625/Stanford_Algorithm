# coding:utf-8

import copy

def permute(numbers):
  results = []
  def permute_back(numbers, selected_numbers):
    if len(selected_numbers) == len(numbers):
      results.append(selected_numbers[:])   # equal to copy.deepcopy()
      return
      
    for num in numbers:
      if num in selected_numbers:
        continue
      selected_numbers.append(num)
      permute_back(numbers, selected_numbers)
      selected_numbers.pop()

  permute_back(numbers, [])
  return results

def nQueen(n):
  def isValid(board, row, col):
    for row_comp in range(0, row):
      if board[row_comp][col] == 'Q':
        return False
      col_comp_left = col - (row - row_comp)
      if col_comp_left >= 0:
        if board[row_comp][col_comp_left] == 'Q':
          return False
      col_comp_right = (n - 1 - col) - (row - row_comp)
      if col_comp_right >= 0:
        if board[row_comp][-(col_comp_right + 1)] == 'Q':
          return False
    return True

  results = []
  board = [['.' for _ in range(n)] for _ in range(n)]

  def nQueenInner(board, row):
    if row == n:
      results.append(copy.deepcopy(board))
      return
    
    for col in range(n):
      if not isValid(board, row, col):
        continue
      board[row][col] = 'Q'
      nQueenInner(board, row+1)

      board[row][col] = '.'  

  nQueenInner(board, 0)
  return results

if __name__ == '__main__':
  # print(permute([1, 2, 3, 4, 5]))
  board = nQueen(8)
  print(len(board))
