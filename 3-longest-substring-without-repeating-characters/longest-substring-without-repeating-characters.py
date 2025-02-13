class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        longest, left = 0, 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while dic[s[i]] > 1:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            longest = max(longest, i-left+1)
        return longest