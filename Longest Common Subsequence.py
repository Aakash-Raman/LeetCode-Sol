def lcs(X , Y): 

    m = len(X) 
    n = len(Y) 
  
    L = [[None]*(n+1) for i in range(m+1)] 

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 

    return L[m][n] 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans = lcs(text1, text2)
        return ans
