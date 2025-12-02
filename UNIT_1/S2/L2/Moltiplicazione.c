// Include penso sia la libreria
#include <stdio.h>

// Devo scitvere una Maain sempliice
int main()
{

    // VARIABILI
    int moltiplicando;
    int moltiplicatore;
    int prodotto;

    printf( "Inserisci il moltiplicando ");
    scanf("%d", &moltiplicando);


    printf( "Inserisci il moltiplicatore ");
    scanf("%d", &moltiplicatore);

    prodotto = moltiplicando * moltiplicatore;

    printf("Risultato: %d\n", prodotto);

}
