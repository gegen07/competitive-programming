#include <bits/stdc++.h>
using namespace std;

int subs_sum(vector<int> set, int sum, int n) {
    vector<vector<int>> subset_sum_matrix(n+1, vector<int>(sum+1));

    for (int i = 0; i < n+1; i++) {
        subset_sum_matrix[i][0] = 1; 
    } 

    for (int j = 1; j < sum+1; j++) {
        subset_sum_matrix[0][j] = 0; 
    } 

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j < set[i-1]) {
                subset_sum_matrix[i][j] = subset_sum_matrix[i-1][j];
            } else if (j >= set[i-1]) {
                subset_sum_matrix[i][j] = subset_sum_matrix[i-1][j] || subset_sum_matrix[i-1][j-set[i-1]];
            }
        }   
    }

    return subset_sum_matrix[n][sum];
}

int main() {
    int sum, n;
    vector<int> set;

    cin >> sum >> n;
    
    int input;
    for (int i = 0; i < n; i++) {
        cin >> input;
        set.push_back(input);
    }
    
    cout << (subs_sum(set, sum, n) == 1 ? "S" : "N") << "\n"; 
}