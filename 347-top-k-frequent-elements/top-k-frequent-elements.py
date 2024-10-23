class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = []
        count = Counter(nums)
        count = sorted(count, key=count.get,reverse= True)
        for key in count:
            if k == 0:
                break
            top.append(key)
            k -= 1
        return top