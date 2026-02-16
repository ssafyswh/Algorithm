#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long N;
    int L;
    cin >> N >> L;

    for (int l = L; l <= 100; l++) {
        long long base = N - (long long)l * (l - 1) / 2;

        if (base >= 0 && base % l == 0) {
            long long x = base / l;
            
            for (int i = 0; i < l; i++) {
                cout << x + i << (i == l - 1 ? "" : " ");
            }
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}