class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        strn = [0] * (n+1)
        
        for start, end, dirn in shifts:
            if dirn == 0:
                strn[start] -= 1
                strn[end+1] += 1
            else:
                strn[start] += 1
                strn[end+1] -= 1
        ans = []
        strn[0] += 26

        for i in range(n):
            strn[i+1] += strn[i]
            ans.append(chr(97 + ((ord(s[i])- 97 + strn[i])%26)))
        return ''.join(ans)