class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sente = list(sentence.split(' '))
        m = len(searchWord)
        for indx,word in enumerate(sente):
            if len(word) >= m and word[:m] == searchWord:
                return indx + 1
        return -1
