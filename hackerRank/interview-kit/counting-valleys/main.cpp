#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
  int counter = 0;
  for (auto it = s.begin(); it != s.end(); ++it) {
    if (*it == 'D') counter--;
    else counter++;
  }

  return counter+1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    cout << result << "\n";

    fout.close();

    return 0;
}

