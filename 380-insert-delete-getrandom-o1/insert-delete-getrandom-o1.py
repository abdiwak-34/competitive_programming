class RandomizedSet:

    def __init__(self):
        self.lis = []
        self.dic = {}        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.lis.append(val)
        self.dic[val] = len(self.lis) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        cur = self.dic[val]
        last = len(self.lis) - 1
        self.lis[cur], self.lis[last] = self.lis[last], self.lis[cur]
        self.dic[self.lis[cur]] = cur
        del self.dic[val]
        self.lis.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.lis)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()