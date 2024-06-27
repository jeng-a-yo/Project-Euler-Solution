#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

bool isPalindromic(long long int n){
    // Check if number is palindromic
    long long int original = n;
    long long int reversed = 0;
    
    while (n > 0) {
        reversed = reversed * 10 + (n % 10);
        n /= 10;
    }
    
    return original == reversed;
}

int main() {
    auto start = high_resolution_clock::now();

    long long int largest_palindrome = 0;
    
    // Iterate over possible products and find largest palindromic number
    for (int i = 999; i >= 100; --i) {
        // Start j from i to avoid checking products more than once
        for (int j = i; j >= 100; --j) {
            long long int product = i * j;
            if (product <= largest_palindrome) break; // No need to continue if further products are smaller
            if (isPalindromic(product)) {
                largest_palindrome = product;
            }
        }
    }
    
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    
    cout << "Largest palindromic number: " << largest_palindrome << endl;
    cout << "Time taken: " << duration.count() << " milliseconds" << endl;

    return 0;
}
