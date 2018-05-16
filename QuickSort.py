# -*- coding=utf-8 -*-
'''
Created on 2018-5-16
快速排序
@author: z00383767
'''
def SimpleSelectionSort(A):
    def findMedianSortedArrays(A):
        Longth_A=len(A)
        left=1
        right=Longth_A
        key=A[0]
        
        if (Longth_A==1):
            return 0,A
        if (Longth_A==2)and(A[0]>A[1]):
            A[0],A[1]=A[1].A[0]
            return 1,A
        if (Longth_A==2)and(A[0]<=A[1]):
            return 0,A
        
        while(left!=right):
            while (left<right):
                left=left+1
                if A[left]>key:
                    break
                
            while (left<right):
                right=right-1
                if A[right]<key:
                    break
                
            if left!=right:   
                A[left],A[right]=A[right],A[left]
            else:
                B=A[1:left]
                B.append(A[0])
                for a in A[left:]:
                    B.append(a)
                return left-1,B
            
    place=findMedianSortedArrays(A)
    print place
    print place[1][0:place[0]]
    print place[1][place[0]:]
    #v=SimpleSelectionSort(place[1])

    #return v
    


if __name__ == '__main__':
    A=[3,2,1]
    SimpleSelectionSort(A)
