class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevrow = self.getRow(rowIndex-1)
        current = [1]
        for i in range(1,len(prevrow)):
            current.append(prevrow[i-1] + prevrow[i])
        current.append(1)
        return current