class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = sorted(zip(heights,names), reverse=True)
        name = [nam for i, nam in height]
        return name