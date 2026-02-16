#include <iostream>

using namespace std;

void solve() {
    int N, F;
    cin >> N >> F;
    int base = (N / 100) * 100;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if ((base + i * 10 + j) % F == 0) {
                cout << i << j;
                return;
            }
        }
    }
}

int main() {
    solve();
    return 0;
}