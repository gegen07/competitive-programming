#include <iostream>
using namespace std;

int main () 
{
  int n;
  cin >> n;

  for (int i=0; i < n; i++) 
  {
    int num;
    cin >> num;

    int soma = 0;

    for (int j = 1; j <= int(num/2); j++)
    {
      if (num % j == 0)
      {
        soma += j;
      }
    }

    if (soma == num)
    {
      cout << num << " eh perfeito" << endl;
    } else
    {
      cout << num << " nao eh perfeito" << endl;
    }
    
  }

  return 0;
}