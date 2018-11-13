#-*- coding=utf-8 -*-
'''
根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

示例:

输入:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        LineNumber = len(board)  # 面板行数
        RowNumber = len(board[0])  # 面板列数
        import copy
        Newboard = copy.deepcopy(board)
        for i in range(0, LineNumber):
            for j in range(0, RowNumber):
                self.AllCells(board, i, j, Newboard)  # 遍历周围细胞
        board=Newboard
        return Newboard

    def AllCells(self, board, i, j, Newboard):  # 遍历周围细胞,获取自身下次状态
        Cells = []
        LivingCells = 0
        DeadCells = 0
        LineNumber = len(board)  # 面板行数
        RowNumber = len(board[0])  # 面板列数a
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if (m < 0) or (n < 0) or (m > LineNumber - 1) or (n > RowNumber - 1):
                    continue
                if board[m][n] == 0:
                    DeadCells = DeadCells + 1
                else:
                    LivingCells = LivingCells + 1

        if board[i][j] == 0:  # 本次为死细胞
            DeadCells = DeadCells - 1
            if LivingCells == 3:
                Newboard[i][j] = 1
        else:
            LivingCells = LivingCells - 1
            if LivingCells < 2 or LivingCells > 3:
                Newboard[i][j] = 0

        return Newboard

board=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
A=Solution()
print A.gameOfLife(board)
