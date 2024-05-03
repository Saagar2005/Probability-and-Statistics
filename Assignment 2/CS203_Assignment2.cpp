#include <iostream>
#include <cmath>

using namespace std;

// Calculates log(n!) using Stirling's Approximation
long double logFact(int n) {
    if (n == 0)
        return 0;
    return n * log(n) + 0.5 * log(n) - n + 0.5 * log(2 * M_PI);
}

// Calculates log of Probabiltity of two people having the same birthday
long double term(int k) {
    return logFact(365) - logFact(365 - k) - k * log(365);
}

// Calculates Probabiltity of two people having the same birthday
long double Prob(int k) {
    long double result = 1;
    for (int i = 0; i < k; ++i) {
        result *= (365.0 - i) / 365.0;
    }
    return 1 - result;
}

// Applies binary search to find minimum value of k for a given p (using probability directly)
int find_k(long double p) {
    int l = 0;
    int r = 365;
    int last_mid = 366;
    if (p == 1)
        return last_mid;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (Prob(mid) > p) {
            r = mid - 1;
            last_mid = mid;
        } else if (Prob(mid) < p) {
            l = mid + 1;
        } else {
            return mid;
        }
    }
    return last_mid;
}

// Applies binary search to find minimum value of k for a given p (using Stirling's Approximation)
int find_k_stirling(long double p) {
    int l = 0;
    int r = 365;
    int last_mid = 366;
    if (p == 1)
        return last_mid;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (term(mid) - log(1 - p) < 0) {
            r = mid - 1;
            last_mid = mid;
        } else if (term(mid) - log(1 - p) > 0) {
            l = mid + 1;
        } else {
            return mid;
        }
    }
    return last_mid;
}

int main() {
    long double p;
    cout << "Let us find the minimum number of people (k) required in a group so that: \nthe probability that atleast two people in the group have the same birthday is not less than p!\n";
    X: cout << "Enter the value of p (Note: p must be in (0,1]): ";
    cin >> p;

    if( !( p>0 && p<=1) )
    {
        cout<<"p must be in (0,1] \n";
        goto X;
    }

    cout << "k calculated using direct formula: ";
    cout << find_k(p) << endl;

    cout << "k calculated using Stirling's Approximation: ";
    cout << find_k_stirling(p) << endl;

    return 0;
}
