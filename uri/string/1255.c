#include <stdio.h>
#include <stdlib.h>

int main () {
  char frase[201];
  int letras[26] = {0};
  int i, j, max, qtd;
  
  scanf("%d ", &qtd);
  
  for (j = 0; j < qtd; j++) {
    fgets(frase, 201, stdin);
    int letras[26] = {0};
    
    for (i = 0; frase[i] != '\0'; i++){
      if (frase[i] >= 65 && frase[i] <= 90) {
        frase[i] += 32; 
      }
    }

    for (i = 0; frase[i] != '\0'; i++){
      if (frase[i] >= 97 && frase[i] <= 122) {
        letras[(frase[i]-97)]++;
      }
    }  
    
    max = letras[0];
    for (i = 1; i < 26; i++) {
      if (max < letras[i]) max = letras[i]; 
    }

    for (i = 0; i < 26; i++) {
      if (letras[i] == max) printf("%c", (i+97));
    }
    printf("\n"); 
  }

  return 0;
}