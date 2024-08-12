class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 


sll = Linkedlist()
nod1 = Node(5)
nod2 = Node(6)
nod3 = Node(7)
nod4 = Node(8)

sll.head = nod1
nod1.next = nod2
nod2.next = nod3
nod3.next = nod4
sll.tail = nod4
