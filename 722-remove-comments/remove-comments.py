class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans =[]
        code = []
        block = False

        for line in source:
            i = 0 
            
            while i < len(line):
                if block:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        block = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i:i+2] == "/*":
                        block = True
                        i += 1
                    elif i + 1 < len(line) and line[i:i+2] == "//":
                        break
                    else:
                        code.append(line[i])
                
                i += 1

            s = ''.join(code)
            if not block and s:
                ans.append(s)
                code.clear()
        return ans
