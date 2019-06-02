#include <bits/stdc++.h>
#include <stdlib.h>

#define loop(arr, size, var) for(int var = 0; var < size; var++)

using namespace std;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr) {
    int primaryDiagonal = 0;
    int secondaryDiagonal = 0;
    
    loop(arr, arr.size(), i) {
        loop(arr[i], arr[i].size(), j) {
            if (i == j) {
                primaryDiagonal += arr[i][j];
            }
            if (i+j == arr[i].size()-1) {
                secondaryDiagonal += arr[i][j];
            } 
        }
    }
    
    return abs(primaryDiagonal-secondaryDiagonal);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = diagonalDifference(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
