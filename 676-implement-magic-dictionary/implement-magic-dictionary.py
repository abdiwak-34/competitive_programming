class MagicDictionary:

    def __init__(self):
        self.bucket = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.bucket[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for candidateword in self.bucket[len(searchWord)]:
            if sum(a!=b for a, b in zip(candidateword,searchWord)) == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)