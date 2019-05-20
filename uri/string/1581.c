#include<stdio.h>
#include<string.h>

int main(){
  int N,i,k,j,A;
  char aux[21];
  
  scanf("%d",&N);
  
  for(i=0;i<N;i++) {
    k=0;
    scanf("%d",&k);
    char lingua[k][21];
    A=0;
    
    for(j=0;j<k;j++){
      scanf("%s",&lingua[j][0]);
      if((strcmp(lingua[0],lingua[j])!=0)){
        A++;
      }
    }
  
    if(A==0){
      printf("%s\n",lingua[0]);
    } else {
      printf("ingles\n");
    }
  }

  return 0;
}