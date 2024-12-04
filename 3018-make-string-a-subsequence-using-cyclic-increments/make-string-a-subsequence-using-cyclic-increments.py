class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ptr1 = ptr2 = 0
        while ptr1 < len(str1) and ptr2 < len(str2):
            if str2[ptr2] == str1[ptr1] or ord(str1[ptr1]) - ord(str2[ptr2]) == -1 or (str1[ptr1] == 'z' and str2[ptr2] == 'a'):
                ptr2 += 1
                ptr1 += 1
            else:
                ptr1 += 1
        
        return ptr2 == len(str2)