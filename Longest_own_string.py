# -*- coding=utf-8 -*-
'''
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        import string
        """
        :type s: str
        :rtype: int
        """
        longth_s=len(s)        
        #最长子串长度
        longest_str_num=0
        #最长子串所对应的具体字符串
        longest_str=[]
        #当前用于存储字符串的缓存
        cash=''
        #第一次字符循环
        longest_str_num=1
        longest_str.append(s[0])
        cash=s[0]
           
        #后续字符循环
        for i in range(0,longth_s-1):
            
            
            pass


    def Judge_exgist(self,str,s):
        ''
        """
        :type str: str
        :type str: one str
        """
        result=str.find(s)
        if result==-1:
            return str+s
        if result==0:
            return [str,str[1:]+s]
        return None
        
if __name__== "__main__":
    A='abcabcbbcdefg'
    LongestString = Solution()
    print LongestString.lengthOfLongestSubstring(A)
