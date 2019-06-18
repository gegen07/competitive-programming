#include <stdio.h>
#include <stdlib.h>

void tabuada(int, int); 

int main() {
  int num;
  scanf("%d", &num);
  tabuada(1, num);
  return 0;
}

void tabuada(int begin, int num) {
  if (begin > 10) {
    return;
  } else {
    printf("%d x %d = %d\n", begin, num, begin*num);
    return tabuada(begin+1, num);
  }
  
  
}