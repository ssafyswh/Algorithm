#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long N, A, B;
        int mid_cnt = 0;
        long long a_total = 0, b_total = 0;
        cin >> N >> A >> B;
        if (A > B) swap(A, B);
        for (int i = 0; i < N; i++) {
            long long target;
            cin >> target;
            if (target - A < B - target) a_total += 2 * (target -A);
            else if (target - A > B - target) b_total += 2 * (B - target);
            else mid_cnt++;
        }
        long long mid_dist = B - A;
        while (mid_cnt--) {
            if (a_total <= b_total) a_total += mid_dist;
            else b_total += mid_dist;
        }
        cout << a_total + b_total << " " << abs(a_total - b_total) << "\n";
    }
    return 0;
}