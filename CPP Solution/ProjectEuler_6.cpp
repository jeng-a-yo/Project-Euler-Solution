#include <iostream>
using namespace std;

int main(){

    long long int sum_of_squares = 0, sum_of_numbers = 0;
    for (int i = 0; i < 100; i++){
        sum_of_numbers += i;
        sum_of_squares += i * i;
    }

    cout << sum_of_numbers  * sum_of_numbers - sum_of_squares << endl;

    return 0;
}