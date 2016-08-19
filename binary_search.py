""" 
	Iterative and Recursive Binary Search
"""

# iterative binary search
def binary_search_itr(arr, num):
	if len(arr):
		low = 0
		high = len(arr)-1
		while low <= high:
			mid = low + (high-low)/2
			if arr[mid] == num :
				return mid
			elif arr[mid] < num:
				low = mid+1
			else:
				high = mid-1
	return -1


# recursive binary search
def binary_search_rec(arr, low, high, num):
	if low <= high:
		mid = low + (high-low)/2
		if arr[mid] == num :
			return mid
		elif arr[mid] < num :
			return binary_search_rec(arr, mid+1, high, num)
		else:
			return binary_search_rec(arr, low, mid-1, num)
	else:
		return -1


if __name__ == '__main__':
	arr = [10,22,34,46,52]
	num = 12
	index = binary_search_itr(arr, num)
	print 'Number found at index %d by iterative search' % (index)
	index = binary_search_rec(arr, 0, len(arr)-1, num)
	print 'Number found at index %d by recursive search' %(index)	
