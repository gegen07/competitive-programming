#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 100000
using namespace std;

/**
 * This algorithm uses disjoint set!
*/
void initSet(int *sets, int n) 
{
  for (int i = 0; i < n; i++)
    sets[i] = i;
}

int findSet(int *sets, int i) 
{
  if (sets[i] == i) return i;
  else return sets[i] = findSet(sets, sets[i]);
}

bool isSameSet(int *sets, int i, int j) 
{
  return findSet(sets, i) == findSet(sets, j);
}

void unionSet(int *sets, int i, int j) 
{
  if (!isSameSet(sets, i, j))
  {
    sets[findSet(sets, i)] = findSet(sets, j);
  }
}

int main () 
{
  int banks, cons;
  int p[MAX];

  cin >> banks >> cons;
  initSet(p, banks);

  for (int i = 0; i < cons; i++)
  {
    int b1, b2;
    char c;

    cin >> c >> b1 >> b2;

    if (c == 'C')
    {
      if (!isSameSet(p, b1, b2))
      {
        cout << 'N' << endl;
      } else
      {
        cout << 'S' << endl;
      }
      
    } else
    {
      unionSet(p, b1, b2);
    }
    
  }

  return 0;
}
