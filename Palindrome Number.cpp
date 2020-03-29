#include <iostream>  
#include<string>  
using namespace std;  
class Solution {
public:
    bool isPalindrome(int x) {
     long int n=x;
        long int rev=0,r;
        if(n<0)
        {
         return false;   
        }
        else
        {
            long int k=n;
            while(n!=0)
            {
              r=n%10;
              rev=rev*10+r;
              n=n/10;
            }
            if(k==rev)
            {
                return true;
                
            }
            else
            {
                return false;
            }
            
        }
   
    }
};
