#include <stdio.h>
#include <stdlib.h>

int tam = 1;

long long int factorial(int n, long long int arr[]) {
  if (tam <= n) {
    int i;
    for (i = tam; i <= n; i++) {
      arr[i] = arr[i-1]*i;
      tam++;
    }
  }
  return arr[n];
}

int main () {
  int fat1, fat2;
  long long int arr[20] = {1};
  while (scanf("%d %d", &fat1, &fat2) != EOF) {
    printf("%lld\n", factorial(fat1, arr) + factorial(fat2, arr));
  }
  return 0;
}