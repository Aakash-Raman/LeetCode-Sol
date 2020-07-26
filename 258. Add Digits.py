class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while(num > 9):
            res = 0
            while(num > 0):
                res += num % 10
                num = num // 10
            num = res
        return res
