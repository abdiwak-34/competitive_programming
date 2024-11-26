class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {val:inx for inx, val in enumerate(arr2)}
        arr1.sort(key= lambda x: (order.get(x, float('inf')), x))
        return arr1