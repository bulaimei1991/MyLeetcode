'''
1,3,4,10
2,5,9,11
6,8,12,15
7,13,14,16
'''

import unittest

class Test(unittest.TestCase):
    def test_FiilinMateix(self):
        A=[[1]]
        B=[[1,2]]
        C=[[1],[2],[3]]
        D=[[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]
        E=[[1,3,4],[2,5,6]]
        self.assertEqual(A,FillinMatrix(1,1))
        self.assertEqual(B,FillinMatrix(1,2))
        self.assertEqual(C,FillinMatrix(3,1))
        self.assertEqual(D,FillinMatrix(4,4))
        self.assertEqual(E,FillinMatrix(2,3))

def FillinMatrix(n,m):
    'input n is the sum number of line & m is the sum number of colume'
    matrix=[[0 for i in range(m)]for i in range(n)]
    Start_num=1

    "the count of numbers in each inclined line"
    inclined_line=[]
    Max=max(m,n)
    Min=min(m,n)
    for i in range(1,m+n):
        if i<Min:
            inclined_line.append(i)
        if Min<=i<=Max:
            inclined_line.append(Min)
        if i>Max:
            inclined_line.append(m+n-i)

    for i in range(0,m+n-1):
        "the Direction of filling in numbers which is inclined,when it is odd whose direction is form bottom to top," \
        "otherwise it is from top to bottom"
        Direction=i%2
        "h is horizontal location in matrix" \
        "v is vertical location in matrix" \
        "Differrnt Direction,Different Starting location"
        if Direction == 0:
            if i < m:
                h=0
            else:
                h=i-m+1
        else:
            if i < n:
                v=0
            else:
                v=i-n+1

        for num in range(0,inclined_line[i]):
            if Direction==0:
                v=i-h
                matrix[h][v]=Start_num
                Start_num=Start_num+1
                h=h+1
            else:
                h=i-v
                matrix[h][v] = Start_num
                Start_num=Start_num+1
                v=v+1
    return matrix

if __name__== "__main__":
   unittest.main()
