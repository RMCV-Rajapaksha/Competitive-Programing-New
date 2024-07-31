# import functools

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = []
#         for _ in range(m):
#             dp.append([0] * n)
        
#         dp[0][0] = 1
    
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
                
#                 val = 0
#                 if i > 0:
#                     val += dp[i-1][j]
#                 if j > 0:
#                     val += dp[i][j-1]
                    
#                 dp[i][j] = val
    
#         return dp[m-1][n-1]

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
      
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1:
            return 0
        

        dp = [[0] * m for _ in range(n)]
        
     
        dp[0][0] = 1
        
 
        for x in range(1, m):
            if obstacleGrid[0][x] == 0:
                dp[0][x] = dp[0][x-1]
        
    
        for y in range(1, n):
            if obstacleGrid[y][0] == 0:
                dp[y][0] = dp[y-1][0]
       
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]

