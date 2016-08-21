def heapify(arr, n, i):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2
	
	if left < n and arr[left] > arr[largest]:
		largest = left
	if right < n and arr[right] > arr[largest]:
		largest = right
	if largest != i:
		arr[largest], arr[i] = arr[i], arr[largest]
		heapify(arr, n, largest)

def heap_sort(arr, n):
	for i in range(n/2, -1, -1):
		heapify(arr, n, i)

	for i in range(n, -1, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)		
	
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	n = len(arr)
	print 'Original Array - ', arr
	heap_sort(arr, n-1)
	print 'Array after Heap Sort - ', arr
