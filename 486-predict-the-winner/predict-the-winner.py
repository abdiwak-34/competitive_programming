class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
       
        def find(left,right):
            if left == right:
                return nums[left]
            
            pick_left = nums[left] - find(left+1, right)
            pick_right = nums[right] - find(left, right-1)

            return max(pick_left, pick_right)
        
        return find(0,len(nums)-1) >= 0