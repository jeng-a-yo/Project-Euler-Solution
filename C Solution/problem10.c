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

    long long int sum = 2;

    for (int i = 3; i < 2000000; i += 2){
        if (IsPrime(i)) sum += i;
    }

    printf("sum = %lld\n", sum);

    return 0;
}