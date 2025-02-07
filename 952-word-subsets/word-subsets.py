class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        max_table = defaultdict(int)
        for word in words2:
            table = defaultdict(int)
            for i in range(len(word)):
                table[word[i]] += 1
            for key, val in table.items():
                max_table[key] = max(max_table[key], val)
        def check(dic1, dic2):
            for key in dic1:
                if dic1[key] > dic2[key]:
                    return False
            return True
        for word in words1:
            table1 = defaultdict(int)
            for i in range(len(word)):
                table1[word[i]] += 1                
            if check(max_table, table1):
                ans.append(word)

        return ans