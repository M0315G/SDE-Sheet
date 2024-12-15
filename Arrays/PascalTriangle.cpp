#include <iostream>
#include <vector>
using namespace std;

// Problem 1: Give me the value for i Row and j Col of the Pascal's Traingle:
// Logic:
// The value of nth row and rth column is governed by the formula (n-1)C(r-1)
// thus we optimise the way we can calculate that value by building a function
// for it. The formula gets reduced to
//          n*(n-1)*(n-2)*.....upto (n-r+1)
//          ---------------------------
//             r*(r-1)*(r-2)*...1

class Solution {
public:
    int compute_n_c_r(int n, int r){
        int result = 1;
        for(int i=0; i<r; i++){
            result *= (n-i);
            result /= (i+1);
        }
        return result;
    }

    int getPascalValue(int row, int col){
        return compute_n_c_r(row-1, col-1);
    }
};

// Problem 2: Given me the complete i'th Row of Pascal's Triangle:
// Logic:
// We can do this using the above function of n_c_r and get all the values
// for the given row and all columns but there is also another optmised version
// for this problem --> We take the 1st value of nth row and formulate the other
// value by adding the numerator and denominator to the previous values
// See video for more details: https://www.youtube.com/watch?v=bR7mQgwQ_o8&t=1068s
class Solution{
public:
    vector<int> getPascalRow(int row){
        long long value = 1;
        vector<int> pascal_row;
        pascal_row.push_back(value);
        for(int i=1; i<row; i++){
            value *= (row-i);
            value /= (i);
            pascal_row.push_back(value);
        }
        return pascal_row;
    }
};

// Problem 3: Give me the whole Pascal's Triangle till i'th row:
// Logic:
// We can either utilize the n_c_r method from solution 1 or get the
// whole row using the solution 2 approach. Better is to go with the solution
// 2 since it's better in time complexity.
class Solution {
public:

    vector<int> generateRow(int rowNum){
        long long value = 1;
        vector<int> pascal_row;
        pascal_row.push_back(value);
        for(int i=1; i<rowNum; i++){
            value *= (rowNum-i);
            value /= (i);
            pascal_row.push_back(value);
        }
        return pascal_row;
    }

    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascalTriangle;
        for(int i=0; i<numRows; i++){
            pascalTriangle.push_back(generateRow(i+1));
        }

        return pascalTriangle;
    }
};