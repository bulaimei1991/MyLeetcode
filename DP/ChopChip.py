#-*- coding=utf-8 -*-
'''
一公司购买长钢条，将其切为短钢条出售，假设切割没有成本，公司希望知道最佳的切割方案！假设我们知道一段长度为i的钢条的价格为pi(i = 1,2,3...),钢条长度均为整英寸，下面给出一个价格表：
长度i	1 	2 	3 	4 	5 	6 	7 	8 	9 	10
价格pi	1 	5 	8 	9 	10	17	17	20	24	30
给定一长度为n的钢条和一张价格表(i =1, 2,3...n)，求切割钢条的方案，使的利润最大,可以不进行切割

'''

class MaxPro(object):
    def DiGui(self,longth,price):
        if longth<=len(price):
            result=[]
            for i in range(1,longth+1):
                if i==1:
                    result.append(price[longth-1])
                else:
                    result.append(self.DiGui(i-1,price)+self.DiGui(longth-i+1,price))
            return max(result)
        else:
            result = []
            for i in range(1, longth):
                    result.append(self.DiGui(i, price) + self.DiGui(longth - i, price))
            return max(result)

    def TuiDao(self):
        pass

price=[1,5,8,9,10,17,17,20,24,30]
A=MaxPro()
print A.DiGui(13,price)

