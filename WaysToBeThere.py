# -*- coding=utf-8 -*-
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        return self.WaysToAPoint(obstacleGrid,len(obstacleGrid)-1,len(obstacleGrid[0])-1)


    def WaysToAPoint(self,obstacleGrid,PointRow,PointLine):
        if obstacleGrid[0][0]==1:
            return 0

        if PointRow==0 and PointLine==0:
            return 1

        if obstacleGrid[PointRow][PointLine]==1:
            return 0

        if (PointRow==0) and (PointLine!=0):
            return self.WaysToAPoint(obstacleGrid,PointRow,PointLine-1)

        if (PointLine==0) and (PointRow!=0):
            return self.WaysToAPoint(obstacleGrid,PointRow-1,PointLine)

        WayAbove=self.WaysToAPoint(obstacleGrid,PointRow,PointLine-1)
        WayLeft=self.WaysToAPoint(obstacleGrid,PointRow-1,PointLine)
        return WayAbove+WayLeft

B=[
  [0,0,0,0,0,0,0,0],
  [0,0,0,1,0,1,1,1],
  [0,0,0,0,0,0,0,0]
]

A=Solution()
print A.uniquePathsWithObstacles(B)







