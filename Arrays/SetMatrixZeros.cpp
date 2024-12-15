class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int col = -1;
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<matrix[i].size(); j++){
                if (matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    if (j==0){
                        col = 0;
                    } else {
                        matrix[0][j] = 0;
                    }
                }
            }
        }

        for (int i=matrix.size()-1; i >= 0; i--){
            for(int j=matrix[i].size() - 1; j >= 0; j--){
                int val1 = matrix[0][j];
                if (j==0){
                    val1 = col;
                }
                if (val1 == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
    }
};