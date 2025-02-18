class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product = [1]
        for i in range(len(nums)):
            pre_product.append(pre_product[-1]*nums[i])
        post_product = [1] * (len(nums)+1)
        for i in range(len(post_product)-2,-1,-1):
            post_product[i] = post_product[i+1] * nums[i]
        result = []
        for i in range(1,len(nums)+1):
            result.append(pre_product[i-1]*post_product[i])
        return result