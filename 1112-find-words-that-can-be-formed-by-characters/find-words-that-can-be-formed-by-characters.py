class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
    
        def ispossible(word, char):
            count1 = Counter(word)
            count2 = Counter(char)
            for key, val in count1.items():
                if count2[key] < val:
                    return False
            return True
    
        for word in words:
            if ispossible(word, chars):
                length += len(word)
        return length