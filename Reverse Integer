class Solution {
public:
    int reverse(int x) {
        long rev=0,r;
       long n=x;
            if(n<0)
            {
             n=n*-1;
             while(n>0)
             {
              r=n%10;
              rev=rev*10+r;
              n=n/10;
             }
             if(rev>2147483647||rev<-2147483647)
                 {
                    return 0;
                 }   
             else
                {
                       return -1*rev;
                }
         
            }
            else
            {
              while(n>0)
              {
              r=n%10;
              rev=rev*10+r;
              n=n/10;
              }
              if(rev>2147483647||rev<-2147483647)
                 {
                    return 0;
                 }   
              else
                {
                       return rev;
                }
            }
        }
        
        
};
