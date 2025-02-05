class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = defaultdict(list)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    common[i+j].append(list1[i])
        return common[min(common.keys())]