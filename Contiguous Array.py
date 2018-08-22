# -*- coding=utf-8 -*-
'''
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组。

示例 1:

输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
注意: 给定的二进制数组的长度不会超过50000。
'''


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLens = len(nums)
        sums = 0
        SumOfnums = [0 for i in range(0, numsLens)]
        MaxLength = 0

        for i in range(0, numsLens):
            if nums[i] == 0:
                nums[i] = -1

        for i in range(0, numsLens):
            sums = sums + nums[i]
            SumOfnums[i]=sums

            if sums == 0:
                MaxLength = i+1
            else:
                try:
                    position = SumOfnums.index(sums)
                    if i - position > MaxLength:
                        MaxLength = i - position
                except:
                    pass
        return MaxLength


A=Solution()
print A.findMaxLength([0,0,1,0,0,0,1,1])
