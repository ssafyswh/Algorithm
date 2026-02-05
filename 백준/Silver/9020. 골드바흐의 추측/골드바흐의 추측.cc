#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<bool> is_prime(10001, true);
    is_prime[0] = false;
    is_prime[1] = false;

    for (int i = 2; i * i <= 10000; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= 10000; j += i) {
                is_prime[j] = false;
            }
        }
    }

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        for (int i = n / 2; i >= 2; i--) {
            if (is_prime[i] && is_prime[n - i]) {
                cout << i << " " << n - i << "\n";
                break;
            }
        }
    }
    return 0;
}