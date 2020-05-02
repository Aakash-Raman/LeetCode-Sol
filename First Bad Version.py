# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while(start < end):
            mid = (start + end)//2
            if(isBadVersion(mid) == True):
                end = mid
            else:
                start = mid+1
        return start
