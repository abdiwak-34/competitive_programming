class Node():
    def __init__(self,key=0,val=0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class Linkedlist():
    def __init__(self):
        self.recent = Node()
        self.least = Node()

        self.least.next = self.recent
        self.recent.prev = self.least
    
    def add(self,node):
        prev_node = self.recent.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.recent
        self.recent.prev = node
    
    def remove(self,node):
        pre_node = node.prev
        next_node = node.next

        pre_node.next = next_node
        next_node.prev = pre_node



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.order = Linkedlist()
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        
        self.order.remove(self.hash[key])
        self.order.add(self.hash[key])
        return self.hash[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.order.remove(self.hash[key])
            self.hash[key].val = value
            self.order.add(self.hash[key])
        else:
            if self.capacity == len(self.hash):
                least_used = self.order.least.next
                self.order.remove(least_used)
                del self.hash[least_used.key]

            newNode = Node(key,value)
            self.order.add(newNode)
            self.hash[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)