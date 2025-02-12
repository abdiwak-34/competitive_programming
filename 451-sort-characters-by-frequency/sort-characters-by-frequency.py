class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count2 = {k:v for k, v in sorted(count.items(), key= lambda item: item[1],reverse=True)}
        ans = []
        for key, val in count2.items():
            ans.append(key*val)
        return ''.join(ans)