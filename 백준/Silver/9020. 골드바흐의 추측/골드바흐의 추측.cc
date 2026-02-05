#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {

    set<int> prime;
    vector<bool> is_prime(10001, true);
    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i < 10001; i++) {
        if (is_prime[i] == false) continue;
        prime.insert(i);
        int oper = 1;
        while (true) {
            oper++;
            if (i * oper <= 10000) is_prime[i * oper] = false;
            else break;
        }
    }
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int u = 0, v = 10000;
        for (int a : prime) {
            if (prime.count(n - a) == 1 && abs(2 * a - n) < abs(u - v)) {
                u = min(a, n - a);
                v = max(a, n - a);
            }
        }
        cout << u << " " << v << "\n";
    }  
}