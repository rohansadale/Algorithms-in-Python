"""
	2-way and 3 way implementation of Quick Sort
"""

def partition(arr, low, high):
	pivot = arr[high]
	fp, bp = low, high-1
	while fp < bp:
		while arr[fp] <= pivot and fp < bp:
			fp += 1
		while arr[bp] > pivot and fp < bp:
			bp -= 1
		if fp < bp:
			arr[fp], arr[bp] = arr[bp], arr[fp]
			
	if arr[fp] > arr[high]:		
		arr[fp], arr[high] = arr[high], arr[fp]
	else:
		fp = high
	return fp

def quick_sort(arr, low, high):
	if low < high:
		pivot = partition(arr, low, high)
		quick_sort(arr, low, pivot-1)
		quick_sort(arr, pivot+1, high)


# 3-way quick sort
def partition3(arr, low, high):
	pivot = arr[high]
	i, j = low, high-1
	p, q = low, high-1
	while True:
		while arr[i] <= pivot and i < j:
			i += 1
		while arr[j] > pivot and i < j:
			j -= 1	
		if i >= j :
			break
		arr[i], arr[j] = arr[j], arr[i]
		
		#print i, j, arr
		if arr[i] == pivot:
			arr[i], arr[p] = arr[p], arr[i]
			p += 1
		if arr[j] == pivot:
			arr[j], arr[q] = arr[q], arr[j]
			q -= 1
	

	if arr[i] > arr[high]:	
		arr[i], arr[high] = arr[high], arr[i]
	#print i, j, low, high, arr 

	j = i-1
	for k in range(low, p):
		arr[k], arr[j] = arr[j], arr[k]
		j -= 1	 
	i = i+1
	for k in range(high-1, q):
		arr[k], arr[i] = arr[i], arr[k]
		i += 1	
	#print j, i, p, q
	#print
	return j, i

		
def quick_sort3(arr, low, high):
	if low < high:
		i, j = partition3(arr, low, high)
		quick_sort3(arr, low, i)
		quick_sort3(arr, j, high)
	

if __name__ == '__main__':
	arr = [10, 7, 8, 9, 5, 1]
	n = len(arr)
	print 'Original Array ', arr
	quick_sort(arr, 0, n-1)
	print 'Array after Two-way Quick Sort ', arr
	
	arr = [10, 7, 8, 9, 5, 5, 5, 1, 1]
	n = len(arr)
	print '\nOriginal Array ', arr
	quick_sort3(arr, 0, n-1)
	print 'Array after Three way Quick Sort ', arr
