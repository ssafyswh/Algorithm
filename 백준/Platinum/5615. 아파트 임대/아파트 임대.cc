#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;

ull power(ull base, ull exp, ull mod) {
    ull res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__uint128_t)res * base % mod;
        base = (__uint128_t)base * base % mod;
        exp /= 2;
    }
    return res;
}

bool miller_rabin(ull n, ull a) {
    if (a % n == 0) return true;
    ull d = n - 1;
    while (d % 2 == 0) {
        if (power(a, d, n) == n - 1) return true;
        d /= 2;
    }
    ull tmp = power(a, d, n);
    return tmp == n - 1 || tmp == 1;
}

bool isPrime(ull n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;
    ull bases[] = {2, 7, 61}; 
    for (ull a : bases) {
        if (n == a) return true;
        if (!miller_rabin(n, a)) return false;
    }
    return true;
}

int main() {
    int N;
    cin >> N;
    int result = 0;
    while (N--) {
        ull A;
        cin >> A;
        if (isPrime(2 * A + 1)) result++;
    }
    cout << result;
    return 0;
}