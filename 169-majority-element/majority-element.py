class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        major = count[nums[0]]
        for key, val in count.items():
            if val > count[major]:
                major = key
        return major