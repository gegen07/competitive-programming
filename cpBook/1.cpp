#include <iostream>

using namespace std;

//Compilation: g++ -std=c++11 -O2 -Wall 1.cpp -o 1
int main() {
  
  /**
   * It is used for improve the speed of cin
  */
  ios::sync_with_stdio(0);
  cin.tie(0);

  
  // int a, b;

  // cin >> a >> b;
  // cout << a << " " << b;
  
  /**
   * getline(input, arg) is used for get input unitl EOF
  */
  string s;
  getline(cin, s);
  cout << s;

  

  return 0;  
}