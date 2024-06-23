#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

list<int> primeFactorization(long long int n, list<int>& primeFactorsList) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            primeFactorsList.push_back(i);
            return primeFactorization(n / i, primeFactorsList);
        }
    }
    // If n is prime and greater than 1
    if (n > 1) {
        primeFactorsList.push_back(n);
    }
    return primeFactorsList;
}

int main() {
    list<int> primeFactorsList = {};
    long long int n = 600851475143LL; // Use LL to denote long long int

    primeFactorization(n, primeFactorsList);

    cout << "prime factorization: ";

    for (auto& element : primeFactorsList) {
        cout << element << " ";
    }
    cout << endl;

    int largest = *max_element(primeFactorsList.begin(), primeFactorsList.end());
    cout << "Largest prime factor: " << largest << endl;

    return 0;
}
