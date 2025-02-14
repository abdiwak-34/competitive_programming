class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_type = defaultdict(int)
        left = maximum = 0
        for right in range(len(fruits)):
            fruit_type[fruits[right]] += 1
            while len(fruit_type) > 2:
                fruit_type[fruits[left]] -= 1
                if fruit_type[fruits[left]] == 0:
                    del fruit_type[fruits[left]]
                left += 1
            maximum = max(maximum, right-left+1)

        return maximum