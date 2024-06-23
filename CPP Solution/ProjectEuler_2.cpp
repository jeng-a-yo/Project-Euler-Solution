#include <iostream>
using namespace std;

int main(){

    long long int previous = 1, current = 1, next = 2, sum = 0;

    while (current < 4000000){
        if (current % 2 == 0){
            sum += current;
        }
        previous = current;
        current = next;
        next = previous + current;
    }

    cout << sum << endl;

    return 0;
}