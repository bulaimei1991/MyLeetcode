#-*- coding=utf-8 -*-
'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        A=[0 for i in range(0,len(triangle))]
        for i in range(0,len(triangle)):
            for j in range(i,-1,-1):
                if j==i:
                    A[j]=A[j-1]+triangle[i][j]
                elif j==0:
                    A[j]=A[0]+triangle[i][j]
                else:
                    A[j]=min(A[j-1],A[j])+triangle[i][j]
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                A[i]=A[i-1]
        return A[-1]

if __name__== "__main__":
    normal = [[2],[3,4],[6,5,7],[4,1,8,3]]
    A=Solution()
    print A.minimumTotal(normal)
