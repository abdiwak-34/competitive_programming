class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_count = Counter(arr)
        for num in arr:
            if num == 0 and arr_count[num] <= 1:
                continue
            if num/2 in arr_count:
                return True
        return False