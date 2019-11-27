def merge(array_a, array_b):
	len_a = len(array_a)
	len_b = len(array_b)
	len_all = len_a + len_b

	i, j = 0, 0
	sorted_array = []

	while (i < len_a) and (j < len_b):
		if i < len_a and array_a[i] < array_b[j]:
			sorted_array.append(array_a[i])
			i +=1
		elif j < len_b and array_b[j] <= array_a[i]:
			sorted_array.append(array_b[j])
			j +=1

	if i < len_a:
		sorted_array.extend(array_a[i:])
	else:
		sorted_array.extend(array_b[j:])

	return sorted_array

def merge_sort(array):
	if len(array) == 1:
		return array
	
	length = len(array)
	mid = length // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	return merge(left, right)

print(merge_sort([5, 2, 1, 3, 8, 6]))