class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            a=str("""""")
            return [a]

        num=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        numberofAlpha=[]

        lenOfresult=1
        for i in digits:
            number=int(i)-2
            lenofNumber=len(num[number])
            numberofAlpha.append(lenOfresult*lenofNumber)
            lenOfresult=lenOfresult*lenofNumber

        result = ["" for i in range(0,lenOfresult)]

        for i in range(0,len(digits)):
            numberIngroup=lenOfresult/(numberofAlpha[i])
            Alpha=num[int(digits[i])-2]

            lenOfAlpha=len(Alpha)
            n=0
            m=0
            while(n<lenOfresult):
                for k in range(0,numberIngroup):
                    result[n]=result[n]+Alpha[m]
                    n=n+1
                m=m+1
                if m==lenOfAlpha:
                    m=0

        return result


number=""
A=Solution()
print A.letterCombinations(number)