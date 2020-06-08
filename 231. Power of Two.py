class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        l,h=0,30
        while l<=h :
            mid=(l+h)//2
            if 2**mid==n :
                return True
            elif 2**mid<n :
                l=mid+1
            else :
                h=mid-1
        return False
