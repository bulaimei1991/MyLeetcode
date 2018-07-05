#-*- coding=utf-8 -*-
'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

'''

class Solution(object):
    def solveSudoku(self, Matrix):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        while True:
            NewMatrix=self.FillinOne(Matrix)
            Matrix=NewMatrix[0]

            if (NewMatrix[1]==8)&(NewMatrix[2]==8):
                return Matrix


    def GetScale(self,i,j):
        if 0<=i<=2:
            Iscale=[0,2]
        if 3<=i<=5:
            Iscale=[3,5]
        if 6<=i<=8:
            Iscale=[6,8]
        if 0<=j<=2:
            Jscale=[0,2]
        if 3<=j<=5:
            Jscale=[3,5]
        if 6<=j<=8:
            Jscale=[6,8]
        return Iscale,Jscale

    def Egist(self,Allnumber):
        if 1 not in Allnumber:
            return 1
        if 2 not in Allnumber:
            return 2
        if 3 not in Allnumber:
            return 3
        if 4 not in Allnumber:
            return 4
        if 5 not in Allnumber:
            return 5
        if 6 not in Allnumber:
            return 6
        if 7 not in Allnumber:
            return 7
        if 8 not in Allnumber:
            return 8
        if 9 not in Allnumber:
            return 9

    def FillinOne(self,Matrix):
        for i in range(0, 9):
            for j in range(0, 9):
                if (i == 8) & (j == 8) & (Matrix[i][j] != '.'):
                    return Matrix,i,j
                if Matrix[i][j] != '.':
                    continue

                Allnumber = []
                for a in range(0, 9):
                    if (Matrix[i][a] != '.') & (Matrix[i][a] not in Allnumber):
                        Allnumber.append(Matrix[i][a])
                    if (Matrix[a][j] != '.') & (Matrix[a][j] not in Allnumber):
                        Allnumber.append(Matrix[a][j])

                Iscale, Jscale = self.GetScale(i, j)
                for b in range(Iscale[0], Iscale[1] + 1):
                    for c in range(Jscale[0], Jscale[1] + 1):
                        if (Matrix[b][c] != '.') & (Matrix[b][c] not in Allnumber):
                            Allnumber.append(Matrix[b][c])

                if len(Allnumber) == 8:
                    Matrix[i][j] = self.Egist(Allnumber)
                    return Matrix,i,j

Matrix=[
        [5,3,'.','.',7,'.','.','.','.'],
        [6,'.','.',1,9,5,'.','.','.'],
        ['.',9,8,'.','.','.','.',6,'.'],
        [8,'.','.','.',6,'.','.','.',3],
        [4,'.','.',8,'.',3,'.','.',1],
        [7,'.','.','.',2,'.','.','.',6],
        ['.',6,'.','.','.','.',2,8,'.'],
        ['.','.','.',4,1,9,'.','.',5],
        ['.','.','.','.',8,'.','.',7,9]
        ]

A=Solution()
print A.solveSudoku(Matrix)