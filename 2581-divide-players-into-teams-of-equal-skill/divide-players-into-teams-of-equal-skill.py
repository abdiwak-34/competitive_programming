class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) -1
        equal_to = skill[left] + skill[right]
        product_sum = 0
        while left < right:
            if skill[left] + skill[right] == equal_to:
                product_sum += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return product_sum