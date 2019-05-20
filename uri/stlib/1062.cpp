#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int main () {
  stack<int> stk;
  int n;

  vector<int> v;

  while (true) {
    cin >> n;
    if (n != 0) {
      while (true) {
        bool stop = false;
        for (int i = 0; i < n; i++) { 
          int num;
          cin >> num;
          if (num == 0 && i == 0) {
            stop = true;
            break;
          } else v.push_back(num); 
        }
        if (stop) {
          cout << endl;
          break;
        } else {
          int curr=0;
          for (int i = 1; i <= n; i++) {
            stk.push(i);   
            while (v.size() > 0 && !stk.empty()) {
              if (stk.top() == v[curr]) {
                stk.pop();
                curr++;
              } else break;
            } 
          }
          (!stk.empty() == 0) ? puts("Yes") : puts("No");
        }
      } 
      v.clear();
    } else {
      break;
    }
  }
    
  return 0;
}
