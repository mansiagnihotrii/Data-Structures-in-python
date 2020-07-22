#!/usr/bin/env python3


import linkedlist
from linkedlist import LinkedList

def remove_duplicate(head):
	previous_node = head
	next_node =  previous_node.next
	temp = set([previous_node.data])
	
	while next_node :
		if next_node.data in temp:
			previous_node.next = next_node.next
		else:
			temp.add(next_node.data)	
			previous_node = next_node
		next_node = next_node.next
		
		
list1 = LinkedList()
head = linkedlist.create_list(list1)

if head is None:
	print("List is empty")
else:
	remove_duplicate(head)
	linkedlist.printlist(list1.head)
		

