class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dic[nums[i] * nums[j]] +=1
        fre = 0

        print(dic)
        for x in dic.values():
            fre += (x*(x-1))*4
        return fre