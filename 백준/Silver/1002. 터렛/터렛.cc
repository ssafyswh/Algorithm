#include <iostream>

using namespace std;

int solve() {
    int x1, y1, r1, x2, y2, r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        if (x1 == x2 && y1 == y2 && r1 == r2) return -1;
        int x = x1 - x2, y = y1 - y2, r_sum = r1 + r2, r_diff = r1 - r2;
        int dist_sq = x * x + y * y, r_sum_sq = r_sum* r_sum, r_diff_sq = r_diff * r_diff;
        if (dist_sq == r_sum_sq || dist_sq == r_diff_sq) return 1;
        if (dist_sq > r_sum_sq || dist_sq < r_diff_sq) return 0;
        return 2;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << solve() << "\n";
    }
    return 0;
}