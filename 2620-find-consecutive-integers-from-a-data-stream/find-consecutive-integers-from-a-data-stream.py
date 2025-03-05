class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k        
        self.queue = deque()
        self.count = 0
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.count += int(num == self.value)
        if len(self.queue) > self.k:
            
            self.count -= int(self.queue.popleft() == self.value)
        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)