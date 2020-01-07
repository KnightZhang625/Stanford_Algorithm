# coding:utf-8

import random

def partition(array):
	length = len(array)
	i = 0
	j = length - 1
	pivot_idx = random.choice(range(length))
	pivot = array[pivot_idx]

	while i < j:
		while i < j and array[i] < pivot:
			i += 1
		array[pivot_idx] = array[i]
		pivot_idx = i
		while i < j and array[j] > pivot:
			j -= 1
		array[pivot_idx] = array[j]
		pivot_idx = j

	array[i] = pivot
	return i

def rSelection(array, i):
	if len(array) == 1:
		return array[0]

	pivot_idx= partition(array)
	if pivot_idx == (i-1):
		return array[pivot_idx]
	elif pivot_idx > (i-1):
		return rSelection(array[:pivot_idx], i)
	elif pivot_idx < (i-1):
		return rSelection(array[pivot_idx+1:], i-(pivot_idx+1))
	else:
		raise ValueError

if __name__ == '__main__':
	array = [5, 2, 1, 10, 20, 15, 12, 30, 6]
	print(rSelection(array, 2))

















