#include <stdio.h>
#include <stdbool.h>


bool IsPrime(int number){

    if (number % 2 == 0) return false;

    for (int i = 3; i * i <= number; i += 2){
        if (number % i == 0) return false;
    }
    return true;
}



int main(){

    int count = 1, number = 3;
    
    while (1){

        if (IsPrime(number)) count++;
        if (count == 10001) break;

        number += 2;
    }

    printf("%d\n", number);

    return 0;
}