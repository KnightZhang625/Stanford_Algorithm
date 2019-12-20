def partition(array, start, end):
	pivot = array[start]

	while start < end:
		while start < end and array[end] >= pivot:
			end -=1
		array[start] = array[end]
		while start < end and array[start] <= pivot:
			start +=1
		array[end] = array[start]

	array[start] = pivot
	return start

def quickSort(array, left, right):
	if left < right:
		i = partition(array, left, right)
		quickSort(array, left, i-1)
		quickSort(array, i+1, right)

if __name__ == '__main__':
	array = [3, 8, 2, 5, 1, 4, 7, 6, 9]
	quickSort(array, 0, len(array) - 1)
	print(array)












	
