# -*- coding=utf-8 -*-
'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
'''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Result=[]
        longth_nums=len(nums)
        for i in range(1,longth_nums+1):
            while i!=nums[i-1]:
                change_pos=nums[i-1]-1
                nums[i-1],nums[change_pos]=nums[change_pos],nums[i-1]
                if nums[i-1]==nums[change_pos]:
                    if nums[i-1] not in Result:
                        Result.append(nums[i-1])
                    break
        return Result

if __name__== "__main__":
    normal = [4, 3, 2, 7, 8, 2, 3, 1]
    A=Solution()
    print A.findDuplicates(normal)
