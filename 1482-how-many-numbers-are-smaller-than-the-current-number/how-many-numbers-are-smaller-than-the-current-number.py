class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num1 in nums:
            count = 0
            for num2 in nums:
                if num2 < num1:
                    count += 1
            ans.append(count)

        return ans