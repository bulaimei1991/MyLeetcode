# -*- coding=utf-8 -*-
'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        import math
        num_l1=0
        num_l2=0
        
        i=0
        while True:
            num_l1=l1.val*(math.pow(10,i))+num_l1
            if l1.next==None:
                break
            else:
                l1=l1.next
            i=i+1
            
        i=0
        while True:
            num_l2=l2.val*(math.pow(10,i))+num_l2
            if l2.next==None:
                break
            else:
                l2=l2.next
            i=i+1
            
        num=int(num_l1+num_l2)
        
        A=[]
        while True:
            A.append(num%10)
            num=(num-num%10)/10
            if num/1<1:
                break
        
        print A
        for i in range(len(A),0,-1):
            if i==len(A):
                l=ListNode(A[i-1])
            else:
                a=l
                l=ListNode(A[i-1])
                l.next=a
            
        return l

def creatLink(set):
    len_set=len(set)
    for i in range(len_set,0,-1): 
        if i==len_set:
            l=ListNode(set[i-1])
        else:
            a=l
            l=ListNode(set[i-1])
            l.next=a
    return l
        

if __name__== "__main__":
    A=[2,4]
    B=[9,9,9,9,9]
    A=creatLink(A)
    B=creatLink(B)

    Add2num = Solution()
    result=Add2num.addTwoNumbers(A,B)
