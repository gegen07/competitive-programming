#include <stdio.h>
#include <stdlib.h>

int main () {
  char phrase[200];  
  
  while (fgets(phrase, 200, stdin) != 0)
  {
    int i, cont=0;
    for (i = 0; phrase[i] != '\0'; i++) {
      if (phrase[i] >= 'a' && phrase[i] <= 'z') {
        phrase[i] = phrase[i]-32;
      }
    }

    char ref = phrase[0];
    int control = 0;
    for (i = 0; phrase[i] != '\0'; i++) {  
      if (phrase[i] == ' ' && ref == phrase[i+1]) {
        if (control == 0) {
          cont++;
          control = 1;
        }
      } else if (phrase[i] == ' ' && ref != phrase[i+1]) {
        ref=phrase[i+1];
        control = 0;
      }    
    }

    printf("%d\n", cont);
  }
  
  return 0;
}