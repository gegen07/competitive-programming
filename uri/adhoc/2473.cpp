#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () 
{
  vector<int> vet(6);
  vector<int> lott(6);

  vector<int>::iterator it;

  for (int i = 0; i < 6; i++)
  {
    cin >> vet[i];
  }
  
  for (int i = 0; i < 6; i++)
  {
    cin >> lott[i];
  }

  int cont = 0;
  for (auto i = lott.begin(); i != lott.end(); i++)
  {
    it = find(vet.begin(), vet.end(), *i);
    if (it != vet.end())
    {
      cont += 1;
    }
  }

  switch (cont)
  {
  case 3:
    cout << "terno" << endl;
    break;
  case 4:
    cout << "quadra" << endl;
    break;
  case 5:
    cout << "quina" << endl;
    break;
  case 6:
    cout << "sena" << endl;
    break;
  default:
    cout << "azar" << endl;
  }

  return 0;
}