class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==""):
            return True
        else:
            t_pointer= 0
            s_pointer= 0
            
            s_len=0
            t_len=0
            
            for i in s:
                s_len+= 1
            for i in t:
                t_len+= 1
            
            for t_pointer in range(0,t_len):
                if(t[t_pointer] == s[s_pointer]):
                    s_pointer+= 1
                    if(s_pointer==s_len):
                        return True
            return False
