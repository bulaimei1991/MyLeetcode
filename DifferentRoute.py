# -*- coding=utf-8 -*-
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1:
            return 1
        if n==1:
            return 1
        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

if __name__== "__main__":
    A=Solution()
    print A.uniquePaths(7,3)
