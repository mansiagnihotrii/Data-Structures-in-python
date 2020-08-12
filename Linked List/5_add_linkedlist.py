'''
	You have two numbers represented by linked list in reverse order. 
	Your task is to output the sum of two integers as linkedlist in reverse order.
	For example, input: (7 -> 1 -> 6) + (5 -> 9-> 2). That is 617 + 295
							 output: (2 -> 1 -> 9). That is 912
	
'''

#!/usr/bin/env python3


import linkedlist
from linkedlist import LinkedList,Node
	
		
def add_lists(head1 ,head2 ,carry=0):
	if head1 == None and head2 == None and carry == 0:
		return None
	result_list = LinkedList()
	value = carry
	if head1 is not None:
		value += head1.data
	if head2 is not None:
		value += head2.data
	result_list.data = value%10
	if head1 is not None or head2 is not None:
		result_list.next = add_lists(None if head1 == None else head1.next, None if head2 == None else head2.next, 1 if value>=10 else 0)
	return result_list 
					


list1 = LinkedList()
head1 = linkedlist.create_list(list1)

list2 = LinkedList()
head2 = linkedlist.create_list(list2)


if head1 is None or head2 is None:
	print("List is empty")
else:
	result_head = add_lists(head1 ,head2 )
	linkedlist.printlist(result_head)
	
		


