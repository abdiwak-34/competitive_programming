class Solution:
    def canChange(self, start: str, target: str) -> bool:
        ptr1 = ptr2 = 0
        n = len(start)
        while ptr1 < n or ptr2 < n:
            while ptr1 < n and start[ptr1] == '_':
                ptr1 += 1
            while ptr2 < n and target[ptr2] == '_':
                ptr2 += 1
            if ptr1 == n or ptr2 == n:
                return ptr1 == ptr2
            if start[ptr1] != target[ptr2]:
                return False
            if start[ptr1] == 'L' and ptr1 < ptr2:
                return False
            if start[ptr1] == 'R' and ptr1 > ptr2:
                return False
            ptr1 += 1
            ptr2 += 1
        return True