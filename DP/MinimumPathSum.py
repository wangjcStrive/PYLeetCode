# -*- coding: utf-8 -*-
# @Time    : 8/1/2018 6:01 PM
# @FileName: MinimumPathSum.py
# Info: 64 Minimum Path Sum.

# 当往两个方向的临时值相等时，该往哪个方向走
# 常规做法是自底向上的计算，先计算出第一行跟第一列的加和，然后for循环计算其他的

import numpy
import sys
import numpy as np

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None:
            return 0
        (m, n) = np.array(grid).shape
        # init 1st row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        # init 1st column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        # init other node
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

    # 递归方法，超时
    def minPathSum_recursion(self, grid, m, n):
        if m==n==0:
            return grid[0][0]
        if m==-1 or n==-1:
            return sys.maxsize

        return grid[m][n] + min(self.minPathSum_recursion(grid, m - 1, n), self.minPathSum_recursion(grid, m, n-1))

    # leetcode 推荐算法
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        # print(dp)
        i = grid[0][0]
        dp[0][0] = i
        # print(dp)
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # print(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return (dp[n - 1][m - 1])


if __name__ == "__main__":
    ins = Solution()
    # input = [[1,7,1], [1,10,1],  [4,2,1]]
    input = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    # print( ins.minPathSum_recursion(input, len(input)-1, len(input[0])-1))
    print(ins.minPathSum(input))
    print(input)