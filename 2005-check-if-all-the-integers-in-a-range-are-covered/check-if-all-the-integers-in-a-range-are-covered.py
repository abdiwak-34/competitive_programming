class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_set = set()
        another = set()
        for y in ranges:
            my_set.update(range(y[0],y[1]+1))
        for i in range(left, right+1):
            another.add(i)
        return another <= my_set