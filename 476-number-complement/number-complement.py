class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        new = '0b'
        for i in range(2, len(binary)):
            new += '0' if binary[i] == '1' else '1'
        return int(new,2)