class Solution:
    def merge(self, left_half,right_half) -> List[int]:
        left, right = 0, 0
        merged = []
        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left += 1
            else:
                merged.append(right_half[right])
                right += 1
        
        merged.extend(left_half[left:])
        merged.extend(right_half[right:])
        return merged
    
    def mergesort(self, left, right, arr):
        if left == right:
            return [arr[left]]
        mid = (left+right)//2
        left_arr = self.mergesort(left,mid,arr)
        right_arr = self.mergesort(mid+1,right,arr)
        return self.merge(left_arr, right_arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        return self.mergesort(left,right, nums)