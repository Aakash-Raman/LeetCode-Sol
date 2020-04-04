class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int m = nums.length;
        int n = nums[0].length;
        int i,j;
        int k=0;
        int[] a=new int[m*n];
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                a[k]=nums[i][j];
                k++;
            }
        }
        if(r*c==m*n)
        {
           int[][] newnums=new int[r][c];
            k=0;
            for(i=0;i<r;i++)
            {
             for(j=0;j<c;j++)
             {
                newnums[i][j]=a[k];
                k++;
             }
            }
            return newnums;
        }
        else
        {
            return nums;
        }
    }
}
