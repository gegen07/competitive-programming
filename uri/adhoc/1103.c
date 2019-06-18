#include <stdio.h>
#include <stdlib.h>

int main() {
  int h1, m1, h2, m2, mtot, htot;

  while (1) {
    scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
    
    if(h1==0 && h2==0 && m1==0 && m2==0) break;
    
    htot = h2-h1;

    if (htot == 0 ) {
      if (m1 < m2) {
        htot = 0;
      } else {
        htot = 24*60;
      }
    } else if (htot < 0) {
      htot = (25-(abs(htot)+1))*60;
    } else { 
      htot = htot * 60;
    }

    mtot = m2-m1;
    if (mtot == 0) {
      mtot = htot;
    } else if (mtot < 0){
      mtot = htot - abs(mtot);
    } else {
      mtot += htot;
    }
    
    printf("%d\n", mtot);
  }

  return 0;
}