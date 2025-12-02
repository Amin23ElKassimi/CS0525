#include <stdio.h>

int main()
{
    int num1, num2;
    float media;

    printf("Inserisci il primo numero: ");
    scanf("%d", &num1);

    printf("Inserisci il secondo numero: ");
    scanf("%d", &num2);

    media = (num1 + num2) / 2.0;

    printf("La media è: %.2f\n", media);

    return 0;
}
