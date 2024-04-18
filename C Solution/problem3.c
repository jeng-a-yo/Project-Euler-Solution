#include <stdio.h>


int main(){

    long long int number = 600851475143;
    int i = 3, maxDivisor = 0;

    while (1){

        while (number % i == 0){

            number /= i;
            maxDivisor = i;

        }

        if (number == 1) break;
        i += 2;

    }

    printf("%d", maxDivisor);

    return 0;
}