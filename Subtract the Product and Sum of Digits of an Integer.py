class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sod = 0
        mod = 1
        k = n
        while(n!=0):
            r = int(n%10)
            sod = sod+r
            mod = mod*r
            n = int(n/10)
        return mod-sod
