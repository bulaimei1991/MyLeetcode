# -*- coding=utf-8 -*-
'''
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
'''

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        situation = [[[0,0]]]
        Allsituation = [[0,0]]
        while True:
            ThisSituation = []
            for i in situation[-1]:
                print i
                a = self.EmptyA(i)
                b = self.EmptyB(i)
                c = self.FullA(x,i)
                print i
                print a
                d = self.FullB(y,i)
                e = self.PullAtoB(x,y,i)
                f = self.PullBtoA(x,y,i)

                if a not in Allsituation:
                    Allsituation.append(a)
                    ThisSituation.append(a)
                if b not in Allsituation:
                    Allsituation.append(b)
                    ThisSituation.append(b)
                if c not in Allsituation:
                    Allsituation.append(c)
                    ThisSituation.append(c)
                if d not in Allsituation:
                    Allsituation.append(d)
                    ThisSituation.append(d)
                if e not in Allsituation:
                    Allsituation.append(e)
                    ThisSituation.append(e)
                if f not in Allsituation:
                    Allsituation.append(f)
                    ThisSituation.append(f)

            situation.append(ThisSituation)
            if ThisSituation==[]:
                break
        return situation

    def EmptyA(self,situationNow):
        situationNow[0] = 0
        return situationNow

    def EmptyB(self,situationNow):
        situationNow[1]=0
        return situationNow

    def FullA(self,x,situationNow):
        situationNow[0]=x
        return situationNow

    def FullB(self,y,situationNow):
        situationNow[1]=y
        return situationNow

    def PullAtoB(self,x,y,situationNow):
        AllWatre=situationNow[0]+situationNow[1]
        situationNow[0]=0
        if AllWatre>=x+y:
            situationNow[1]=x+y
        else:
            situationNow[1]=AllWatre
        return situationNow

    def PullBtoA(self,x,y,situationNow):
        AllWatre = situationNow[0] + situationNow[1]
        situationNow[1] = 0
        if AllWatre >= x + y:
            situationNow[0] = x + y
        else:
            situationNow[0] = AllWatre
        return situationNow

if __name__== "__main__":
    My=Solution()
    print My.canMeasureWater(3,5,4)
