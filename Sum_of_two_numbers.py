# -*- coding=utf-8 -*-
'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
'''

class Solution(object):
    def twoSum(self,nums,target):
        len_nums=len(nums)
        for i in range(0,len_nums):
            for j in range(i+1,len_nums):
                if nums[i]+nums[j]==target:
                    return [i,j]


if __name__== "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    A=Solution()
    print A.twoSum(nums,target)



