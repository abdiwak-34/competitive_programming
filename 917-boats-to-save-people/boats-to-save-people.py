class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        count = 0
        while left <= right:
            current_weight = people[left] + people[right]
            if current_weight <= limit:
                left += 1
                right -= 1
            else:
                right -=1
            count += 1
        return count