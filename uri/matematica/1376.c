#include <stdio.h>
#include <stdlib.h>

int main() {
  int numSucessor, dimR, dimC, numBatalhas;
  int matDim[100][100] = {-1};
  
  while (1) {
    scanf("%d %d %d %d", &numSucessor, &dimR, &dimC, &numBatalhas);
    if (numSucessor == 0 && dimR == 0 && dimC == 0 && numBatalhas == 0) break;

    int i, j, k;
    for (i = 0; i < dimR; i++) {
      for (j = 0; j < dimC; j++) {
        scanf("%d", &matDim[i][j]); 
      }
    }

    int l, m;
    for (i = 0; i < numBatalhas; i++){
      int arrPosic[100][100];
      /* Set de uma matriz auxiliar*/
      for (l = 0; l < dimR; l++) {
        for (m = 0; m < dimC; m++) {
          arrPosic[l][m] = matDim[l][m];
        }
      }

      /* Fazendo as contas para as posições adjacentes */
      for (l = 0; l < dimR; l++) {
        for (j = 0; j < dimC; j++) {
          if (j-1 >= 0) {
            if (((matDim[l][j]+1) % numSucessor) == matDim[l][j-1]){
              arrPosic[l][j-1] = matDim[l][j];
            }               
          }
          if (l-1 >= 0) {
            if (((matDim[l][j]+1) % numSucessor) == matDim[l-1][j]){
              arrPosic[l-1][j] = matDim[l][j];
            }  
          }
          if (l+1 < dimR) {
            if (((matDim[l][j]+1) % numSucessor) == matDim[l+1][j]){
              arrPosic[l+1][j] = matDim[l][j];
            }  
          }
          if (j+1 < dimC) {
            if (((matDim[l][j]+1) % numSucessor) == matDim[l][j+1]){
              arrPosic[l][j+1] = matDim[l][j];
            }  
          }
        }
      }

      /* Mudando a matriz principal */
      for (j = 0; j < dimR; j++) {
        for (k = 0; k < dimC; k++) {
          if (matDim[j][k] != arrPosic[j][k]) {
            matDim[j][k] = arrPosic[j][k];
          }
        }
      }
    }

    for (i = 0; i < dimR; i++) {
      for (j = 0; j < dimC; j++) {
        if (j == dimC -1) printf("%d", matDim[i][j]); 
        else printf("%d ", matDim[i][j]); 
      }
      printf("\n");
    }
  }
  
  return 0;
}
