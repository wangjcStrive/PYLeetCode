# -*- coding: utf-8 -*-
# @Time    : 8/7/2018 4:56 PM
# @FileName: UniquePathsII.py
# Info: 62. Unique Paths && 63. Unique Paths II


class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP = [[-1 for i in range(n)] for i in range(m)]
        # for j in range(n):
        #     DP[0][j] = 1
        # for i in range(m):
        #     DP[i][0] = 1
        DP = [[1 for i in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
        return DP[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        :boundary:
            1. start or end with 1: [[1]]=>0. [[0, 1]]=>0
            2. first row/column has 1
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 \
                or obstacleGrid[m-1][n-1] == 1 \
                or obstacleGrid == None:
            return 0

        DP = [[1 for i in range(n)] for i in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                DP[0][j:n] = [0 for i in range(n-j+1)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for x in range(i, m):
                    DP[x][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
        return DP[-1][-1]


if __name__ == '__main__':
    ins = Solution()
    input = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    # print(ins.uniquePaths(7, 3))
    print(ins.uniquePathsWithObstacles(input))
