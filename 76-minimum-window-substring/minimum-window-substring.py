class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_s = defaultdict(int)
        count_t = Counter(t)
        def is_substring(count_t, count_s):
            for key in count_t:
                if count_t[key] > count_s[key]:
                    return False
            return True
        
        left = right = 0
        window =''
        while left <= right and right < len(s):
            count_s[s[right]] += 1
            while right-left+1 >= len(t) and is_substring(count_t, count_s):
                if not window or len(window) > len(s[left:right+1]):
                    window = s[left:right+1]
                count_s[s[left]] -= 1
                left +=1
            right += 1
        return window