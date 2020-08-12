'''
def merge_sort(array):
	size = len(array)
	
	return array
	
	
array = list(map(int,input("Enter elements of array: ").split()))
print("Sorted array:",merge_sort(array))
'''
# Python program for implementation of MergeSort 
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1
		print(arr)

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

# driver code to test the above code 
if __name__ == '__main__': 
	arr = [5,4,3,2,1] 
	print ("Given array is", end ="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end ="\n") 
	printList(arr) 

# This code is contributed by Mayank Khanna 

