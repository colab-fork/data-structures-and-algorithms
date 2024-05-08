class Node:
    
    def __init__(self, data): #every single node has two attributes -> data, next
        self.data = data
        self.next = None
        
    def  __repr__(self): #used to represent the objects of a class in the form of a string
        return self.data


class LinkedList:
    
    def __init__(self):
        self.head = None #only information you need is where the L list starts
    
    def __repr__(self): 
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)



"""
>>> %Run -c $EDITOR_CONTENT
>>> llist = LinkedList()
>>> llist
None
>>> first_node = Node('a')
>>> llist.head = first_node
>>> llist
a->None
>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist
a->b->c->None
>>> 

"""
