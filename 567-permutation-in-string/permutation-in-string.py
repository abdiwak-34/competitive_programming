class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_permutation(dic1,dic2):
            for key in dic2:
                if dic1[key] != dic2[key]:
                    return False
            return True
        k = len(s1)
        count_s2 = Counter(s2[:k-1])
        count_s1 = Counter(s1)
        for i in range(k,len(s2)+1):
            count_s2[s2[i-1]] += 1
            if is_permutation(count_s2,count_s1):
                return True
            count_s2[s2[i-k]] -= 1
        return False