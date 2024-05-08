class Node:
    
    def __init__(self, data): #every single node has two attributes -> data, next
        self.data = data #data
        self.next = None #pointer
        
    def  __repr__(self): #used to represent the objects of a class in the form of a string
        return self.data


class LinkedList:
    
    def __init__(self):
        self.head = None #only information you need is where the L list starts, indicates we have an empty list
    
    def add(self, data): #takes data as a parameter
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next: #traverses until the end
                current = current.next
            current.next = new_node
    
    def __repr__(self): 
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    
    

"""

A linked list is a linear data structure where elements are not stored next to each other in memory. Unlike and array, elements in a linked list use pointers or references to each other to keep the list intact.
Like arrays or traditional lists, linked lists are an ordered collection of objects. Linked lists stand apart from lists in how they store elements in memory. While regular lists like arrays and slices use a contiguous memory block to store references to their data linked lists store references or pointers as part of each element.

>>> lis = LinkedList()
>>> lis
None
>>> f = Node('a')
>>> s = Node('b')
>>> lis.head = f
>>> f.next = s
>>> lis
a->b->None
>>> lis.add('c')
>>> lis
a->b->c->None

"""
