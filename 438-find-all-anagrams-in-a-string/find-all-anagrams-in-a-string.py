class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        ans = []
        p_count = Counter(p)
        s_count = Counter()
        k = len(p)
        for right in range(len(s)):
            s_count[s[right]] += 1
            if right >= k:
                if s_count[s[right-k]] == 1:
                    del s_count[s[right-k]]
                else:
                    s_count[s[right-k]] -= 1
            if s_count == p_count:
                ans.append(right-k + 1)
        return ans