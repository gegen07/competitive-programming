#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
  int Q, D, P;

  while (scanf("%d", &Q) && Q != 0) {
    scanf("%d %d", &D, &P);
    if (D == 0 || P == 0) break;
    
    int expression = trunc(P*((Q*D)/(double)((P-Q))));

    printf("%d pagina", expression);
    if (expression != 1)
      printf("s");
    printf("\n");
  }
  
  return 0;
}