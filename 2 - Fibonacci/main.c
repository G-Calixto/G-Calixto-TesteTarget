#include <stdio.h>
#include <math.h>

int main(){
    int n;

    printf("Informe o numero que deseja checar se pertence ou nao a sequencia de Fibonacci\n");
    scanf("%d", &n);

    double nElevado = 5*pow(n,2);
    if(sqrt(nElevado+4) - (int)sqrt(nElevado+4) == 0.0 ||sqrt(nElevado-4) - (int)sqrt(nElevado-4) == 0.0 ){
        printf("O numero %d existe na sequencia de Fibonacci :)\n", n);
    } else{
        
        printf("O numero %d nao existe na sequencia de Fibonacci :(\n", n);
    }

    return 0;
}