# -*- coding=utf-8 -*-
'''

给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        LongestNumber=0
        Longeststrings={}

        if len(s)==0:
            return LongestNumber

        for i in range(0,len(s)):
            if Longeststrings.has_key(str(s[i])):
                OldPosition=Longeststrings[str(s[i])]
                Longeststrings = {}
                for j in range(OldPosition+1,i+1):
                    Longeststrings[str(s[j])]=j
                Longeststrings[str(s[i])] = i

            else:
                Longeststrings[str(s[i])] = i
                if len(Longeststrings) > LongestNumber:
                    LongestNumber = len(Longeststrings)

        return LongestNumber

B='abcabbda'
A=Solution()
print A.lengthOfLongestSubstring(B)