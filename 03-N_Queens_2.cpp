#include <iostream>
#include <vector>
using namespace std;

int N;

// Print solution
void printBoard(vector<vector<int>>& board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Branch and Bound function
bool solveNQueens(vector<vector<int>>& board, int row,
                  vector<bool>& cols,
                  vector<bool>& diag1,
                  vector<bool>& diag2) {

    // All queens placed
    if (row == N)
        return true;

    for (int col = 0; col < N; col++) {

        // Check if position is safe
        if (!cols[col] &&
            !diag1[row - col + N - 1] &&
            !diag2[row + col]) {

            // Place queen
            board[row][col] = 1;
            cols[col] = true;
            diag1[row - col + N - 1] = true;
            diag2[row + col] = true;

            // Recur for next row
            if (solveNQueens(board, row + 1, cols, diag1, diag2))
                return true;

            // Backtrack
            board[row][col] = 0;
            cols[col] = false;
            diag1[row - col + N - 1] = false;
            diag2[row + col] = false;
        }
    }

    return false;
}

int main() {
    cout << "Enter N: ";
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N, 0));

    vector<bool> cols(N, false);
    vector<bool> diag1(2 * N - 1, false); // row-col
    vector<bool> diag2(2 * N - 1, false); // row+col

    if (solveNQueens(board, 0, cols, diag1, diag2))
        printBoard(board);
    else
        cout << "No solution exists." << endl;

    return 0;
}
