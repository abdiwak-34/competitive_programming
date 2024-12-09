class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        is_special = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i] % 2 != nums[i + 1] % 2:
                is_special[i] = 1
        prefix_special = [0] * n
        for i in range(1, n):
            prefix_special[i] = prefix_special[i - 1] + is_special[i - 1]
        result = []
        for fromi, toi in queries:
            if toi == fromi:
                result.append(True)
            else:
                total_special_pairs = prefix_special[toi] - prefix_special[fromi]
                result.append(total_special_pairs == (toi - fromi))
        
        return result