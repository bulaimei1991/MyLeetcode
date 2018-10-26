# -*- coding=utf-8 -*-
'''
Created on 2018-5-16
快速排序
@author: z00383767
'''
import unittest

class Test(unittest.TestCase):
    def test_findMedianSortedArrays(self):
        A=[1,2,3]
        B=[3,2,1]
        C=[1]
        D=[1,2]
        E=[2,1]
        F=[5,2,5,4,6]
        self.assertEqual((0,[1,2,3]),findMedianSortedArrays(A,0,len(A)-1))
        self.assertEqual((2,[3,2,1]),findMedianSortedArrays(B,0,len(B)-1))
        self.assertEqual((1,[3,2,1]),findMedianSortedArrays(B,0,len(B)-2))
        self.assertEqual((0,[1]),findMedianSortedArrays(C,0,len(C)-1))
        self.assertEqual((0,[1,2]),findMedianSortedArrays(D,0,len(D)-1))
        self.assertEqual((1,[2,1]),findMedianSortedArrays(E,0,len(E)-1))
        self.assertEqual((3,[5,2,5,4,6]),findMedianSortedArrays(F,0,len(F)-1))
    
    def test_SimpleSelectionSort(self):  
        A=[1,2,3]
        B=[3,2,1]
        C=[1]
        D=[1,2]
        E=[2,1]
        F=[5,2,5,4,6]
        self.assertEqual(([1,2,3]),SimpleSelectionSort(A,0,len(A)-1))
        self.assertEqual(([1,2,3]),SimpleSelectionSort(B,0,len(B)-1))
        self.assertEqual(([1]),SimpleSelectionSort(C,0,len(C)-1))
        self.assertEqual(([1,2]),SimpleSelectionSort(D,0,len(D)-1))
        self.assertEqual(([1,2]),SimpleSelectionSort(E,0,len(E)-1))
        self.assertEqual(([2,4,5,5,6]),SimpleSelectionSort(F,0,len(F)-1))

def findMedianSortedArrays(A,left,right):
    left1=left
    right1=right
    key=A[left]
    
    if (left==right):
        return left,A
    if (right-left==1):
        if A[left]>A[right]:
            return right,A
        else:
            return left,A
    
    while(left1!=right1):
        while (left1<right1):
            left1=left1+1
            if A[left1]>key:
                break
        
        if (left1==right1)and(A[left1]>key):
            return right1-1,A
        if (left1==right1)and(A[left1]<=key):
            return right,A
        
        while (left1<right1):
            if A[right1]<key:
                break
            right1=right1-1           

        if (left1==right1):
            return left1-1,A
            
        if left1!=right1:
            A[left1],A[right1]=A[right1],A[left1]

def SimpleSelectionSort(A,left,right):
    if left<right:
        place=findMedianSortedArrays(A,left,right) 
        A.insert(place[0]+1, A[left])
        del A[left]
        A=SimpleSelectionSort(A,left,place[0]-1)
        A=SimpleSelectionSort(A,place[0]+1,right)
    return A

def QuickSort(arrey):
    if len(arrey)<=1:
        return arrey
    else:
        FirstHalf=[i for i in arrey[1:] if i<arrey[0]]
        LastHalf=[i for i in arrey[1:] if i>=arrey[0]]
        return QuickSort(FirstHalf)+[arrey[0]]+QuickSort(LastHalf)

if __name__ == '__main__':
    #unittest.main()
    A=[2,3,1,4,2]
    print QuickSort(A)
