# -*- coding=utf-8 -*-
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

A=Solution()
print A.consecutiveNumbersSum(16)
