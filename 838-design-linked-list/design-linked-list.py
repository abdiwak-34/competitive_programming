class Node:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        head = self.dummy.next
        temp = head
        counter = 0

        while temp and counter < index:
            temp = temp.next
            counter += 1
        
        if counter == index and temp:
            return temp.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        itr = self.dummy

        while itr.next:
            itr = itr.next

        itr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        itr = self.dummy
        counter = 0
        while itr.next and counter < index:
            itr = itr.next
            counter += 1
        
        if counter == index:
            new_node.next = itr.next
            itr.next = new_node          

    def deleteAtIndex(self, index: int) -> None:
        itr = self.dummy
        counter = 0
        while itr.next and counter < index:
            itr = itr.next
            counter += 1
        
        if counter == index and itr.next:
            itr.next = itr.next.next