#include <stdio.h>

int GCD(int x, int y){

    if (x > y) return GCD(y, x);
    if (y % x == 0) return x;
    return GCD(x, y % x);

}

int LCM(int x, int y){
    return x * (y / GCD(x, y));
}

int main(){

    int multiple = 1;

    for (int i = 2; i <= 20; i++){
        multiple = LCM(i, multiple);
    }

    printf("%d\n", multiple);

    return 0;
}