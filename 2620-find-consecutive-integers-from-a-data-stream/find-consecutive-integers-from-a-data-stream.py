class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0        
        self.queue = deque()
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
        if len(self.queue) > self.k:
            po = self.queue.popleft()
            if po == self.value:
                self.count -= 1
        return len(self.queue) == self.k and self.count == self.k               



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)