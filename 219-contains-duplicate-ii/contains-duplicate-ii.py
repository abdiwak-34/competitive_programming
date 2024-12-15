class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter()
        for indx, val in enumerate(nums):
            if val in count and abs(indx - count[val]) <= k:
                return True
            else:
                count[val] = indx
        return False