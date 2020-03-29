class Solution {
    public boolean isPalindrome(String s) {
        String fixed_string="";
        for(char c:s.toCharArray()){
            if(Character.isDigit(c)||Character.isLetter(c)){
                fixed_string+=c;
            }
        }
        fixed_string=fixed_string.toLowerCase();
        
        int a=0;
        int b=fixed_string.length()-1;
        
        while(a<=b)
        {
            if(fixed_string.charAt(a)!=fixed_string.charAt(b))
            {
                return false;
            }
            a=a+1;
            b=b-1;
        }
        return true;
    }
}
