class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = set()
        left = 0
        for right in range(len(nums)):
            if right > k:
                count.remove(nums[left])
                left += 1
            if nums[right] in count:
                return True
            count.add(nums[right])
        return False