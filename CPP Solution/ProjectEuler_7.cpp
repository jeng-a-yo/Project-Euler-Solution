#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long int number) {
    if (number <= 1) return false;
    if (number <= 3) return true;
    if (number % 2 == 0 || number % 3 == 0) return false;
    for (long long int i = 5; i * i <= number; i += 6) {
        if (number % i == 0 || number % (i + 2) == 0)
            return false;
    }
    return true;
}

int main() {
    int count = 1; // Count the prime number 2
    long long int number = 1;

    while (count < 10001) {
        number += 2; // Check only odd numbers
        if (isPrime(number)) {
            count++;
        }
    }

    cout << "The 10001st prime number is: " << number << endl;

    return 0;
}
