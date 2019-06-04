#include <stdio.h>
#include <stdlib.h>

int maxValue(int a, int b) {
  return ((a+b+abs(a-b))/2);
}

int main() {
  int A, B, C;
  scanf("%d %d %d", &A, &B, &C);
  printf("%d eh o maior\n", maxValue(maxValue(A,B), C));
  return 0;
}