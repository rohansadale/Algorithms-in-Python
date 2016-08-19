"""
	Sorting Algorithms
		- Selection Sort
		- Bubble Sort
		- Insertion Sort
"""

# Time Complexity O(n*n) | Space Complexity - O(1)
def selection_sort(arr):
	if len(arr) < 2:
		return arr
		
	for i in range(len(arr)-1):
		idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[idx]:
				idx = j
		arr[i], arr[idx] = arr[idx], arr[i]
	return arr



# Time Complexity O(n*n) | Space Complexity - O(1)
def bubble_sort(arr):
	if len(arr) < 2:
		return arr

	for i in range(len(arr)):
		swap = False
		for j in range(len(arr)-i-1):
			if arr[j+1] < arr[j]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap = True
		if not swap:
			break
	return arr
	

# Time Complexity O(n*n) | Space Complexity - O(1)
def insertion_sort(arr):
	if len(arr) < 2:
		return arr

	for i in range(1, len(arr)):
		num = arr[i]
		j = i-1

		while j >= 0 and arr[j] > num:
			arr[j+1] = arr[j]
			j = j-1
		arr[j+1] = num
	
	return arr


if __name__ == '__main__':
	arr = [65, 12, 1, 34, 23]
	
	print 'Selection Sort'
	arr_s = selection_sort(arr) 
	print arr_s

	print '\nBubble Sort'
	arr_b = bubble_sort(arr)
	print arr_b

	print '\nInsertion Sort'
	arr_i = insertion_sort(arr)
	print arr_i
