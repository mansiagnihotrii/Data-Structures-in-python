'''
	Find kth to last element in a Singly Linked List
'''

#!/usr/bin/env python3


import linkedlist
from linkedlist import LinkedList
		
def find_el(head,k):
	start = head
	if start is None:
		return 0
	else:
		index = find_el(start.next,k) + 1		
		if index == k:
			print(start.data)
		return index


list1 = LinkedList()
head = linkedlist.create_list(list1)

k = int(input())
if head is None:
	print("List is empty")
else:
	find_el(head,k)
	
		


