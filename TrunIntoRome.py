#-*- coding=utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result=""
        numberRange = [1000, 500, 100, 50, 10, 5, 1]
        number = {"1":"I","5":"V","10":"X","50":"L","100":"C","500":"D","1000":"M"}

        specialNumber = {"IIII":"IV","VIIII":"IX","XXXX":"XL","LXXXX":"XC","CCCC":"CD","DCCCC":"CM"}
        specialNumberRange = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]

        for i in numberRange:
            thisresult = num / int(i)
            renmainsResult = num % int(i)

            for j in range(0,thisresult):
                result=result+number[str(i)]
                num=renmainsResult

        for k in specialNumberRange:
            if result.find(k)!=-1:
                result=result.replace(k,specialNumber[k])

        return result

A=Solution()
print A.intToRoman(3999)