#-*- coding=utf-8 -*-
'''
神奇的字符串 S 只包含 '1' 和 '2'，并遵守以下规则：

字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。

字符串 S 的前几个元素如下：S = “1221121221221121122 ......”

如果我们将 S 中连续的 1 和 2 进行分组，它将变成：

1 22 11 2 1 22 1 22 11 2 11 22 ......

并且每个组中 '1' 或 '2' 的出现次数分别是：

1 2 2 1 1 2 1 2 2 1 2 2 ......

你可以看到上面的出现次数就是 S 本身。

给定一个整数 N 作为输入，返回神奇字符串 S 中前 N 个数字中的 '1' 的数目。

注意：N 不会超过 100,000。

示例：

输入：6
输出：3
解释：神奇字符串 S 的前 6 个元素是 “12211”，它包含三个 1，因此返回 3。
'''
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        Result = 1
        Array = [1]
        Arraybag = [[1]]
        ArraybagSame = [1]
        if n == 0:
            return 0

        if n <= 3:
            return Result

        i = 1
        while (i <= n - 1):
            if i == 1:
                Array.append(2)
            else:
                number1 = ArraybagSame[i]
                Array.append(number1)
                if number1 == 1:
                    Result = Result + 1

            if (Array[i] == 1) & (Arraybag[i - 1][0] == 1):
                Arraybag.append([2])
                ArraybagSame.append(2)
            elif (Array[i] == 2) & (Arraybag[i - 1][0] == 1):
                Arraybag.append([2, 2])
                ArraybagSame.append(2)
                ArraybagSame.append(2)
            elif (Array[i] == 1) & (Arraybag[i - 1][0] == 2):
                Arraybag.append([1])
                ArraybagSame.append(1)
            else:
                Arraybag.append([1, 1])
                ArraybagSame.append(1)
                ArraybagSame.append(1)
            i = i + 1

        return Result

A=Solution()
print A.magicalString(6)