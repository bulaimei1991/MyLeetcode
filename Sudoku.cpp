//============================================================================
// Name        : Sudoku.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	cout << "!!!Hello World111!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

class Solution {
public:
    void solveSudoku(vector<vector<char> > &board)
	{
		solve2(board);
	}

	bool solve2(vector<vector<char> > &board, int row = 0, int col = 0)
	{
		if (row == 9) return true;

		int nr = col==8? row+1:row;
		int nc = col==8? 0:col+1;

		if (board[row][col] != '.')
		{
			if (solve2(board, nr, nc)) return true;
		}
		else
		{
			for (char i = '1'; i <= '9'; i++)
			{
				board[row][col] = i;
				if (isValid(board, row, col) && solve2(board, nr, nc)) return true;
			}
			board[row][col] = '.';
		}
		return false;
	}

	const static int SQUNUM = 9;
	const static int NUM = 3;

	bool isValid(vector<vector<char> > &board, int row, int col)
	{
		int sRow = row / NUM;
		int sCol = col / NUM;
		for (int i = 0; i < SQUNUM; i++)
		{
			if (i != col && board[row][col] == board[row][i])
				return false;
			if (i != row && board[row][col] == board[i][col])
				return false;
			//注意这里的计算公式：先定位小九宫大位置，然后小九宫里面的小位置
			int r = sRow*NUM + i/NUM, c = sCol*NUM + i%NUM;
			if (!(r == row && c == col) && board[row][col] == board[r][c])
				return false;
		}
		return true;
	}
};
