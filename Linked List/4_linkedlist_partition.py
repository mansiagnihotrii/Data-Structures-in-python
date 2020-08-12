'''
	Given a linked list and an element , say 'x'. 
	Divide the same list so that the left part of the list has all the elements less that 'x' 
		and right part has all elements greater than or equal to 'x'.
	
'''

#!/usr/bin/env python3


import linkedlist
from linkedlist import LinkedList,Node
	
		
def partition_list(head,element):
	start = head
	new = LinkedList()
	new.head = Node(start.data)
	start = start.next
	while start:
		if start.data >= element:
			linkedlist.insert_end(new.head,start.data)		
		else:
			new.head = linkedlist.insert_beg(new.head,start.data)
		start = start.next
	return new.head
			


list1 = LinkedList()
head = linkedlist.create_list(list1)

element = input("Enter partition element: ")
if head is None:
	print("List is empty")
else:
	new_head = partition_list(head,element)
	linkedlist.printlist(new_head)
	
	
		


