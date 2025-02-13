class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind_dic = defaultdict(int)
        for i in range(len(s)):
            ind_dic[s[i]] = i
        end, size = 0,0
        ans = []
        for i in range(len(s)):
            end = max(end,ind_dic[s[i]])
            size += 1
            if end == i:
                ans.append(size)
                size = 0
        return ans