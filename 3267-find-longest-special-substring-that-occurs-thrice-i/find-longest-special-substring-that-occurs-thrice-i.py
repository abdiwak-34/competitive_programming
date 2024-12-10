class Solution:
    def maximumLength(self, name: str) -> int:
        rep = Counter()
        maxim =  -1
        for i in range(len(name)):
            for j in range(i, len(name)):
                sub  =  name[i:j+1]
                if len(set(sub)) == 1:
                    rep[sub] +=1
                if rep[sub] >=3:
                    maxim =  max(maxim, len(sub))
        return maxim