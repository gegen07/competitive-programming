#include <iostream>
#include <cmath>

using namespace std;

int main () {
  int R1, R2, X1, X2, Y1, Y2;

  while (cin >> R1 >> X1 >> Y1 >> R2 >> X2 >> Y2) {
    double dist = sqrt((pow((float)(X2-X1), 2)+(pow((float)(Y2-Y1), 2))));
    if (dist+R2 <= R1) {
      cout << "RICO" << endl;
    } else {
      cout << "MORTO" << endl;
    }
  }
}