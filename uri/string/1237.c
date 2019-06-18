#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int, int);
int lcs(char*, char*, int, int);

int main() {
  char x[101];
  char y[101];

  while (fgets(x, 101, stdin) != 0 && fgets(y, 101, stdin) != 0) {
     int m = strlen(x);
    int n = strlen(y);

    printf("%d\n", lcs(x, y, m, n));
  }
 
  return 0;
}

int max(int a, int b) {
  return a > b ? a : b; 
}

int lcs(char *x, char *y, int m, int n) {
  int lcsuff[m+1][n+1];
  int result = 0;
  int i, j;

  for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++) {
      if (i == 0 || j == 0) {
        lcsuff[i][j] = 0;
      } else if (x[i-1] == y[j-1]){
        lcsuff[i][j] = lcsuff[i-1][j-1]+1;
        result = max(result, lcsuff[i][j]);
      } else lcsuff[i][j] = 0;
    }
  }

  return result;
}