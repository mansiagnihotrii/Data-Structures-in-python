def insertion_sort(array):
	size = len(array)
	for i in range(1,size):
		key = array[i]
		j = i-1
		while j>=0 and key<array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = key
	return array
	
	
array = list(map(int,input("Enter elements of array: ").split()))
print("Sorted array:",insertion_sort(array))
