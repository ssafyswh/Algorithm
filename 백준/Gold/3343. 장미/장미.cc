#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    long long N, A, B, C, D;
    cin >> N >> A >> B >> C >> D;
    if (B * C > D * A) {
        swap(A, C);
        swap(B, D);
    }
    long long result = 2e18;

    for (int i = 0; i < A; i++) {
        long long cost_cd = (long long)i * D;
        long long remaining_n = N - (long long)i * C;

        if (remaining_n <= 0) {
            result = min(result, cost_cd);
        } else {
            long long buy_a = (remaining_n + A - 1) / A;
            result = min(result, cost_cd + buy_a * B);
        }
    }

    cout << result << endl;
    return 0;
}