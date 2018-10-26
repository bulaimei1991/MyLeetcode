# -*- coding=utf-8 -*-
'''

'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length=len(temperatures)
        result=[i for i in range(0,length)]

        for i in range(0,length):
            i=length-i-1
            if i==length-1:
                result[i]=0
                continue

            



        return result

temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
A=Solution()
A.dailyTemperatures(temperatures)