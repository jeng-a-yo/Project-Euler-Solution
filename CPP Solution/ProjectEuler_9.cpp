#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    bool found = false;

    for (a = 1; a < 1000 / 3; ++a) {
        for (b = a + 1; b < 1000 / 2; ++b) {
            c = 1000 - a - b;
            if (a * a + b * b == c * c) {
                found = true;
                break;
            }
        }
        if (found) {
            break;
        }
    }

    if (found) {
        cout << "The Pythagorean triplet is: " << a << ", " << b << ", " << c << endl;
        cout << "The product abc is: " << a * b * c << endl;
    } else {
        cout << "No Pythagorean triplet found for which a + b + c = 1000." << endl;
    }

    return 0;
}
