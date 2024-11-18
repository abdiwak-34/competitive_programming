class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for book in bookings:
            first, last, seet = book[0], book[1], book[2]
            answer[first-1] += seet
            if last < n:
                answer[last] -= seet
        for i in range(1,n):
            answer[i] += answer[i-1]
        return answer
