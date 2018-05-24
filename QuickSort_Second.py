'''
Created on 2018-4-17

@author: z00383767
'''
class Solution(object):
    def findMedianSortedArrays(self, nums,left1,right1):
        key=nums[left1]
        left,right=left1,right1
        while left<right:
            while left<right and nums[right]>=key:
                right=right-1
            if key>nums[right]:
                nums[left]=nums[right]
                nums[right]=key
            
            while left<right and nums[left]<=key:
                left=left+1
            if nums[left]>key:
                nums[right]=nums[left]
                nums[left]=key
        return left

    def sort(self,v,left,right):
        if left<right:
            p=self.findMedianSortedArrays(v,left,right)
            v=self.sort(v,left,p-1)
            v=self.sort(v,p+1,right)
        return v
        
        
nums = [1,2,1,3,9,8,4,8,5,1,3,6,7]
a=Solution()
print a.sort(nums,0,len(nums)-1)
