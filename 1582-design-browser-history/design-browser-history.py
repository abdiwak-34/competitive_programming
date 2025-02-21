class Node():
    def __init__(self,url=None):
        self.url = url
        self.prev = None
        self.next = None
    

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.current = Node(homepage)
        self.head.next = self.current
        self.current.prev = self.head        
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.current.next = newNode
        newNode.prev = self.current

        self.current = newNode
        self.current.next = None
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != self.head:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)