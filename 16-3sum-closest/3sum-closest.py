class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = defaultdict(int)
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                three_sum = nums[i] + nums[left] +nums[right]
                if three_sum == target:
                    return target
                elif three_sum > target:
                    right -= 1
                else:
                    left += 1
                closest[abs(target-three_sum)] = three_sum
        return closest[min(closest.keys())]