import sys

def count_sort(array_a, array_b):
	array_c = []
	len_a = len(array_a)
	len_b = len(array_b)
	len_c = len_a + len_b

	a_i = 0
	b_j = 0
	count = 0
	for c_i in range(len_c):
		if array_a[a_i] < array_b[b_j]:
			array_c.append(array_a[a_i])
			a_i += 1
			if a_i == len_a:
				break
		elif array_a[a_i] > array_b[b_j]:
			array_c.append(array_b[b_j])
			b_j += 1
			count += (len_a - a_i)
			if b_j == len_b:
				break

	if a_i < len_a:
		array_c += array_a[a_i : ]
	if b_j < len_b:
		array_c += array_b[b_j : ]

	return array_c, count

def count_inversions(array):
	if len(array) == 1:
		return array, 0
	
	mid = len(array) // 2

	array_a, count_1 = count_inversions(array[ : mid])
	array_b, count_2 = count_inversions(array[mid : ])
	array_c, count_3 = count_sort(array_a, array_b)

	return array_c, count_1 + count_2 + count_3

if __name__ == '__main__':
	test_array = [5, 3, 6, 1, 2, 8]
	sorted_array, count = count_inversions(test_array)
	print(sorted_array, count)