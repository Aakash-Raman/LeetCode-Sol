class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # highlight differences with XOR
        tmp = x^y
        # count the number of 1's in the diff
        counter = 0
        while tmp != 0:
            # clear the least significant bit
            tmp &= tmp-1
            counter += 1
        return counter
