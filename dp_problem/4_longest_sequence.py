# coding:utf-8

def longestSequence(nums):
  length = [1 for _ in range(len(nums))]
  batchtrace = {0:0}
  for i in range(len(nums)):
    for j in range(i):
      if nums[i] > nums[j]:
        if length[j] + 1 > length[i]:
          length[i] = length[j] + 1
          batchtrace[i] = j
        else:
          batchtrace[i] = i      

  max_length = max(length)
  idx = length.index(max_length)
  selected_index = [idx]
  prev_idx = batchtrace[idx]
  while prev_idx != batchtrace[prev_idx]:
    selected_index.append(prev_idx)
    prev_idx = batchtrace[prev_idx]
  selected_index.append(batchtrace[prev_idx])

  return max(length), list(reversed(selected_index))

if __name__ == '__main__':
  print(longestSequence([1, 4, 3, 4, 2]))