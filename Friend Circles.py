#-*- coding=utf-8 -*-
'''
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:

输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
示例 2:

输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

N 在[1,200]的范围内。
对于所有学生，有M[i][i] = 1。
如果有M[i][j] = 1，则有M[j][i] = 1。
'''

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        NumberOfStudents = len(M)
        AllFriendCycles = []  # 所有朋友圈
        WhichCycleBelongsTo = [0 for i in range(0, NumberOfStudents)]  # 每一个同学属于第几个朋友圈
        NumberOfCycle = 0  # 朋友圈个数

        for i in range(0, NumberOfStudents):
            # 判断此朋友圈是否属于之前存在的某个朋友圈
            IsOldFriendCycle = self.JudgeCycleBelongsTo(i,NumberOfStudents, M, WhichCycleBelongsTo)
            if IsOldFriendCycle == 0:  # 新朋友圈
                NumberOfCycle = NumberOfCycle + 1
                AllFriendCycles.append(M[i])
                for j in range(0, NumberOfStudents):
                    if (M[i][j] == 1):
                        WhichCycleBelongsTo[j] = NumberOfCycle
            else:  # 老朋友圈
                for j in range(0, NumberOfStudents):
                    if (M[i][j] == 1):
                        AllFriendCycles[IsOldFriendCycle-1][j] = 1
                        WhichCycleBelongsTo[j] = IsOldFriendCycle

        return NumberOfCycle

    # 判断此朋友圈是否属于之前存在的某个朋友圈,返回值为0则为新朋友圈,非0为老朋友圈
    def JudgeCycleBelongsTo(self,i, NumberOfStudents, M, WhichCycleBelongsTo):
        for j in range(0, NumberOfStudents):
            if (M[i][j] == 1) and (WhichCycleBelongsTo[j] != 0):
                return WhichCycleBelongsTo[j]
        return 0


    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """


        return len(M)

    #两个朋友圈合并
    def CombineTwoCycle(self,Cycle1,Cycle2):
        pass

M=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
A=Solution()
print A.findCircleNum(M)