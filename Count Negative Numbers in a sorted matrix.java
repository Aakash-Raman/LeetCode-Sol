class Solution {
    public int countNegatives(int[][] grid) {
        int n = grid.length; //Row Length
        int m = grid[0].length; //Column Length
        int i,j;
        int s=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(grid[i][j]<0)
                {
                    s += 1;
                }
            }
        }
        return s;
        
    }
}
