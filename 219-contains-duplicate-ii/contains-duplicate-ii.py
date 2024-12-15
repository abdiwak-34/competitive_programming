class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter()
        left = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            if right > k:
                if count[nums[left]] == 1:
                    del count[nums[left]]
                else:
                    count[nums[left]] -= 1
                left += 1
            if count[nums[right]] >= 2:
                return True
        return False