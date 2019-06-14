#include <stdio.h>
#include <stdio_ext.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char num, contrato[200];
  scanf("%c", &num);
  scanf("%s", contrato);
  while (num != '0') {
    char novo[200];
    int i, j=0, control=0;
    
    for (i = 0; contrato[i] != '\0'; i++){
      if (contrato[i] != num) {        
        novo[j] = contrato[i];
        j++;
      }
    }
    novo[j]='\0';

    char contratoNovo[200];
    char ref='0';
    j = 0;
    for (i = 0; i < strlen(novo); i++) {
      if (novo[i] != ref) {
        control=1;
      }
      
      if (control == 1) {
        contratoNovo[j] = novo[i];
        j++;
      }    
    }
    contratoNovo[j] = '\0';

    if (strlen(contratoNovo) == 0) {
      contratoNovo[0] = '0';
      contratoNovo[1] = '\0';
    }
    printf("%s\n", contratoNovo);
    scanf(" %c", &num);
    scanf("%s", contrato);
  }

  return 0;
}