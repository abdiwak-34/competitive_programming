class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        def helper(s):
            res = []
            if len(s) >= k:
                return s
            for i in s:
                res.append(chr(((ord(i) -96)%26)+97))
            return helper(s + ''.join(res))
        return helper(s)[k-1]