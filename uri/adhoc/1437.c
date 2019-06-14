#include <stdio.h>
#include <stdlib.h>

int main () {
  char comandos[1000], rosa[4] = {'N', 'O', 'S', 'L'};
  int num, i, qtd;
  int posicao=0;

  scanf("%d", &qtd);
  while (qtd != 0)
  {
    scanf("%s", comandos);
    for (i = 0; comandos[i] != '\0'; i++) {
      if (comandos[i]=='D') {
        posicao--;
      } else posicao++;
      if (posicao < 0) posicao=3;
      posicao %= 4;
    }

    printf("%c\n", rosa[posicao]);
    posicao = 0;
    scanf("%d", &qtd);
  }

  return 0;
}