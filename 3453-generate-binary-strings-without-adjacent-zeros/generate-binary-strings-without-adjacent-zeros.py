class Solution:
    def validStrings(self, n: int) -> List[str]:
        answer = []
        def backtrack(string):
            if len(string) > 1 and string[-1] == '0' and string[-2] == '0':
                return
            if len(string) == n:
                answer.append(''.join(string[:]))
                return

            string.append('0')
            backtrack(string)
            string[-1] = '1'
            backtrack(string)
            string.pop()
        backtrack([])
        return answer