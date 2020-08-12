#!/usr/bin/env python3

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
#Create linked list
def create_list(list1):
	size = int(input("Size of linked list:"))
	for _ in range(size):
		new = input("Enter value:   ")
		if list1.head is None:
			list1.head = Node(new)
		else:
			insert_end(list1.head,new)
	return list1.head
	

#Traversing the list    
def printlist(head):
		value = head
		if value is None:
			print("List is empty")
		else:
			while value is not None:
				print(value.data)
				value = value.next
      
#Insertion at beginning of list
def insert_beg(head,value):
	start = head
	node = Node(value)
	start = node
	node.next = head
	return start

#Insertion at end of list
def insert_end(head,value):
	start = head
	node = Node(value)
	while start.next is not None:
		start = start.next
	start.next = node
	node.next = None
	

#Insertion at any position in list
def insert_position(head,value,position):
	start = head
	node = Node(value)
	while position>1:
		start = start.next
		position -=1
	#start points to current position
	node.next = start.next
	start.next = node
	
	
	
#Deletion at beginning of list
def delete_beg(head):
	head = head.next
	return head

#Deletion at end of list
def delete_end(head):
	start = head
	while start.next.next is not None:
		start = start.next
	start.next = None
	

#Deletion at any position in list
def delete_position(head,position):
	start = head
	while position>1:
		start = start.next
		position -=1
	#start points to current position-1
		start.next = start.next.next

#Reverse the list
def reverse(head):
	prev_node = head
	next_node = prev_node.next
	while next_node :
		temp = next_node.next
		next_node.next = prev_node
		prev_node = next_node
		next_node = temp
	head.next = None
	return prev_node
	



	
	


