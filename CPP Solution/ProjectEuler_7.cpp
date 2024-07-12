#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Function to generate prime numbers using the Sieve of Eratosthenes
void generatePrimes(vector<bool>& isPrime, int limit) {
    fill(isPrime.begin(), isPrime.end(), true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= sqrt(limit); ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j < limit; j += i) {
                isPrime[j] = false;
            }
        }
    }
}

// Function to find the nth prime number
int findNthPrime(int n) {
    // Estimate an upper limit for the nth prime number using the approximation n log n + n log log n
    int limit = n * log(n) + n * log(log(n));
    vector<bool> isPrime(limit, true);
    generatePrimes(isPrime, limit);

    int count = 0;
    for (int i = 2; i < limit; ++i) {
        if (isPrime[i]) {
            ++count;
            if (count == n) {
                return i;
            }
        }
    }
    return -1; // If not found within the limit
}

int main() {
    int n = 10001;
    int prime = findNthPrime(n);
    cout << "The " << n << "th prime number is " << prime << endl;
    return 0;
}
