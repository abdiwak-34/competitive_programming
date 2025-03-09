class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque()
        left = len(deck)-1
        while left >= 0:
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(deck[left])
            left -= 1
        return list(ans)