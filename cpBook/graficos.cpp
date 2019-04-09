#include <iostream>

using namespace std;

void grafico1() {
  for (int i = 19; i >= 1; i--) { 
    if (i%2 != 0) {
      int espacos = (19-i)/2;

      for (int j = 0; j < espacos; j++) {
        printf(" ");
      }

      for (int j = i; j > 0; j--) {
        printf("*");
      }

      printf("\n");
    }
  }
  return;
}

void grafico2() {
  for (int i = 10; i >= 2; i--) { 
    if (i%2 == 0) {
      int espacos = (10-i)/2;

      for (int j = 0; j < espacos; j++) {
        printf(" ");
      }

      for (int j = i; j > 0; j--) {
        printf("*");
      }

      printf("\n");
    }
  }
  for (int i = 2; i <= 10; i++) { 
    if (i%2 == 0) {
      int espacos = (10-i)/2;

      for (int j = 0; j < espacos; j++) {
        printf(" ");
      }

      for (int j = i; j > 0; j--) {
        printf("*");
      }

      printf("\n");
    }
  }
  return;
}

void grafico3() {
  for (int i = 10; i >= 1; i--) {
    for(int j = i; j > 0; j--) {
      printf("*");
    }
    printf("\n");
  }
  
  return;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int escolha;

  cin >> escolha;

  switch(escolha) {
    case 1:
      grafico1();
      break;
    case 2:
      grafico2();
      break;
    case 3:
      grafico3();
      break;
    default:
      cout << "Not implemented Yet!";
  }

  return 0;
}
