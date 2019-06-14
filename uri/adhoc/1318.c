#include <stdio.h>
#include <stdlib.h>
int main () {
  int N, M;
  
  while (1) {
    scanf("%d %d", &N, &M);
    if (N == 0 && M==0) break;
  
    int vet[10000]={0};
    int i, cont=0;
    for (i = 0; i < M; i++) {
      int num;
      scanf("%d", &num);
      
      if (vet[num-1] == 1) cont++;
      vet[num-1]++;
    } 

    printf("%d\n", cont);
    
  }

  return 0;
}