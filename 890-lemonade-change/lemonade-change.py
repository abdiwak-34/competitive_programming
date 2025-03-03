class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = count10 = 0
        for i in range(len(bills)):
            count5 += int(bills[i] == 5)
            count10 += int(bills[i] == 10)
            if bills[i] == 10:
                if count5 > 0:
                    count5 -= 1
                else:
                    return False
            if bills[i] == 20:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 > 2:
                    count5 -= 3
                else:
                    return False
        return True