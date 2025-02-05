class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        ans = []
        for wor in words:
            word = wor.lower()
            if set(word) <= set1 or set(word) <= set2 or set(word) <= set3:
                ans.append(wor)
        return ans