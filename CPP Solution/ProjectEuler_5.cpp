#include <iostream>
using namespace std;

// Function to calculate the greatest common divisor (GCD) using Euclid's algorithm
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to calculate the least common multiple (LCM)
int lcm(int a, int b) {
    return (a / gcd(a, b)) * b; // LCM(a, b) = (a / GCD(a, b)) * b
}


int main(){

    long long ans = 2;
    for (int i = 3; i < 20; i++) {
        ans = lcm(ans, i);
    }

    cout << ans << endl;

    return 0;
}