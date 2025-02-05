class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            let = list(word)
            key = ''.join(sorted(let))
            dic[key].append(word)
        return [val for val in dic.values()]