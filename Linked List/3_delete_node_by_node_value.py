'''
	Delete any node between start and end of Singly Linked List, given only access to that node ONLY.
'''

#!/usr/bin/env python3


import linkedlist
from linkedlist import LinkedList
		
def delete_el(node):
	if node and node.next:
		node.data , node.next.data = node.next.data,node.data
		node.next = node.next.next
		linkedlist.printlist(head)
	else:
		print("Can't delete")


list1 = LinkedList()
head = linkedlist.create_list(list1)

element = input("Enter element to be deleted: ")
if head is None:
	print("List is empty")
else:
	start = head
	while start:
		if start.data == element:
			break
		start=start.next
	if start is None:
		print("Element not in the list")
	else:
		delete_el(start)
	
	
		


