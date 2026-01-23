#include <iostream>
#include <vector>
#include <cmath>
#include <cfloat>

using namespace std;

int N;
pair<long long, long long> dots[20];
double solve(int idx, int plus, int minus, long long x, long long y) {
    if (idx == N) {
        return sqrt((double)x * x + (double)y * y);
    }
    double result = DBL_MAX;
    int nx = dots[idx].first, ny = dots[idx].second;
    if (plus != 0) {
        result = min(result, solve(idx + 1, plus - 1, minus, x + nx, y + ny));
    }
    if (minus != 0) {
        result = min(result, solve(idx + 1, plus, minus - 1, x - nx, y - ny));
    }
    return result;
}

int main() {
    cout << fixed;
    cout.precision(12);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> N;
        for (int i = 0; i < N; i++){
            cin >> dots[i].first >> dots[i].second;
        }
        cout << solve(0, N / 2, N / 2, 0, 0) << "\n";
    }
    return 0;
}