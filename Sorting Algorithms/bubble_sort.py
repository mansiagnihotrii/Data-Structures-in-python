def bubble_sort(array):
	size = len(array)
	for i in range(size):
		swapping = False
		for j in range(size-i-1):
			if array[j]>array[j+1]:
				array[j] ,array[j+1] = array[j+1] ,array[j]
				swapping = True
		if swapping == False:
			break
	return array
	
	
array = list(map(int,input("Enter elements of array: ").split()))
print("Sorted array:",bubble_sort(array))
