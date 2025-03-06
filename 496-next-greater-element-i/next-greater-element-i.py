class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next1 = defaultdict(int)
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    next1[nums2[i]] = stack[-1]
                stack.append(nums2[i])
        ans = []
        for i in range(len(nums1)):
            if nums1[i] not in next1:
                ans.append(-1)
            else:
                ans.append(next1[nums1[i]])
        return ans