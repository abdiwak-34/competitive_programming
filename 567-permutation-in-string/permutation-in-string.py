class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        n = len(s1)
        s2_count = {}
        left = 0
        for i in range(len(s2)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            if i - left + 1 > n:
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    s2_count.pop(s2[left])
                left += 1
            if s2_count == s1_count:
                return True
        return False