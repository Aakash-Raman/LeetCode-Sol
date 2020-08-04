class Solution(object):
    def isPowerOfFour(self, num):
        while num%4==0 and num>0: num = num/4
        return True if num==1 else False
