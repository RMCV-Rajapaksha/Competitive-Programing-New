class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path(i,j):
            if i==0 or j==0:
                return 1
            elif i<0 or j<0 or i==m or j==n:
                return 0
            else:
                return path(i-1,j)+path(i,j-1)
            
        return path(m-1,n-1)