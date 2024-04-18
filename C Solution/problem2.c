#include <stdio.h>

int main(){

    int i = 0, j = 1, k, sum = 0;

    while (k < 4000000){

        i = j;
        j = k;
        k = i + j;

        if (k % 2 == 0) sum += k;

    }

    printf("sum = %d\n", sum);

    return 0;
}