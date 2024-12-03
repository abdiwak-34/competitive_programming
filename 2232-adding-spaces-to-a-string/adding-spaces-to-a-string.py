class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ''
        ptr1 = ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(spaces):
            if ptr1 != spaces[ptr2]:
                new_str += s[ptr1]
                ptr1 += 1
            else:
                new_str += ' ' + s[ptr1]
                ptr1 += 1
                ptr2 += 1
        if ptr1 < len(s):
            new_str += s[ptr1:]
        return new_str