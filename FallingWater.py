#-*- coding=utf-8 -*-
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0

        highest=[0,0]
        SumWater=0
        for i in range(0,len(height)):
            if height[i]==highest[0]:
                highest.append(i)
            elif height[i]>highest[0]:
                highest[0]=height[i]
                highest[1]=i
                del highest[2:]

        position=[0,0]
        MaxLevelWate=height[0]
        for i in range(1,highest[1]+1):
            if height[i]>MaxLevelWate:
                position[1]=i
                SumWater=SumWater+self.countWater(height,position)
                position[0]=i
                MaxLevelWate=height[i]

        if len(highest)>2:
            for i in range(1,len(highest)-1):
                SumWater=SumWater+self.countWater(height,[highest[i],highest[i+1]])

        position=[0,len(height)-1]
        MaxLevelWate = height[-1]
        for i in range(len(height)-2,highest[-1]-1,-1):
            if height[i]>MaxLevelWate:
                position[0]=i
                SumWater=SumWater+self.countWater(height,position)
                position[1]=i
                MaxLevelWate=height[i]

        return SumWater


    def countWater(self,height,position):
        Minlevel=min(height[position[0]],height[position[1]])
        Sum=0
        for i in range(position[0]+1,position[1]):
            Sum=Sum+Minlevel-height[i]
        return Sum

if __name__== "__main__":
    normal = [2,1,1]
    A=Solution()
    print A.trap(normal)