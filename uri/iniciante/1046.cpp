#include <iostream>
using namespace std;

int main () {
  int hrIni, hrFin, tempJogo;

  cin >> hrIni >> hrFin;

  if (hrIni > hrFin)
  {
    tempJogo = 24 - hrIni + hrFin;
  }
  else if (hrIni < hrFin)
  {
    tempJogo = hrFin - hrIni;
  }
  else
  {
    tempJogo = 24;
  }

  cout << "O JOGO DUROU " << tempJogo << " HORA(S)" << endl;

  return 0;
}