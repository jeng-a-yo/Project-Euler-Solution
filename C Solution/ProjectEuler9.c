#include <stdio.h>

int main(){

    for (int i = 1; i < 1000; i++) {
        for (int j = i + 1; j < 1000; j++) {
            for (int k = j + 1; k < 1000; k++) {
                if ((i + j + k) == 1000 && (i * i + j * j == k * k)) printf("%d %d %d %d\n", i, j, k, i * j * k);
            }
        }
    }

    return 0;
}