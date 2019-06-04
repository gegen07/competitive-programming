#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main() {
 
  while (true) {
    char phrase[1050];
    fgets(phrase, 1050, stdin);
    if (phrase[0] == '*') break;
    else {
      int i=0;
      while (phrase[i]) {
        phrase[i] = tolower(phrase[i]);
        i++;
      }
      char ref = phrase[0];
      bool isTautogram = true;

      for (i = 0; phrase[i] != '\0'; i++) {
        if (phrase[i] == ' ' && phrase[i+1] != ref) {
          isTautogram = false;
          break;
        }
      }
      
      if (isTautogram) printf("Y\n");
      else printf("N\n");      
    }
  }
    
  return 0;

}