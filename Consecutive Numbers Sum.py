# -*- coding=utf-8 -*-
'''
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
说明: 1 <= N <= 10 ^ 9
'''
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        NumberOfInt = 0
        i = 1

        if N == 1:
            return 1

        while True:
            Chushu = N / i
            Yushu = N % i

            if Yushu==0:                                #余数为0
                if i % 2 != 0:                          #正整数组元素个数为奇数
                    NumberOfInt = NumberOfInt + 1
                    number = [j for j in range(Chushu-(i-1)/2,Chushu+(i-1)/2+1)]
                    if 1 in number:                    #正整数组中出现1，终止程序
                        break

                else:                                   #正整数组元素个数为偶数
                    number = [j for j in range((Chushu - i/2+1),((Chushu - i/2+1) + i))]
                    Totalnumber = sum(number)
                    if (Totalnumber==N) or (Totalnumber -i ==N):
                        NumberOfInt = NumberOfInt + 1
                    if 2 in number:                     #正整数组中出现1，终止程序
                        break

            else:                                       #余数不为0
                if i % 2 != 0:                          #正整数元素个数为奇数
                    number = [j for j in range(Chushu-(i-3)/2,Chushu-(i-3)/2+i)]
                    Totalnumber = sum(number)
                    if (Totalnumber==N) or (Totalnumber -i ==N):
                        NumberOfInt = NumberOfInt + 1
                    if 2 in number:             #正整数组中出现1，终止程序
                        break

                else:                                   #正整数元素个数为偶数
                    number = [j for j in range(Chushu-(i/2-1),Chushu-(i/2-1)+i)]
                    Totalnumber = sum(number)
                    if (Totalnumber==N):
                        NumberOfInt = NumberOfInt + 1
                    if 1 in number:             #正整数组中出现1，终止程序
                        break
            i = i + 1
        return NumberOfInt

    def consecutiveNumbersSum2(self, N):
        """
        :type N: int
        :rtype: int
        """
        import math

        number=0

        n=float(1)
        N=float(N)
        MAXn=0.5+math.sqrt(1+8*N)/2

        while(n<=MAXn):
            a=float(N/n-n/2+0.5)
            if (int(a)==a) and (a>0):
                number=number+1
            n=n+1

        return number

A=Solution()
print A.consecutiveNumbersSum2(16)
