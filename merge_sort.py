"""
	Merge Sort algorithm implementation
"""
def merge(arr, low, mid, high):
	n1 = mid - low + 1
	n2 = high - mid

	a1 = []
	a2 = []
	for i in range(n1):
		a1.append(arr[low+i])
	for i in range(n2):
		a2.append(arr[mid+i+1])		

	#print a1, a2
	i,j,k = 0,0,low
	while i < n1 and j < n2:
		if a1[i] < a2[j]:
			arr[k] = a1[i]
			k += 1
			i += 1
		else:
			arr[k] = a2[j]
			k += 1
			j += 1
	
	while i < n1:
		arr[k] = a1[i]
		k += 1
		i += 1
	while j < n2:
		arr[k] = a2[j]
		k += 1
		j += 1


def merge_sort(arr, low, high):
	if low < high:
		mid = low + (high-low)/2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid+1, high)
		merge(arr, low, mid, high) 

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print 'Original Array - ', arr
	merge_sort(arr, 0, len(arr)-1)
	print 'Array after Merge Sort - ', arr
