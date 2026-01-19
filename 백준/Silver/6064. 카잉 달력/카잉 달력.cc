// 6064 카잉달력

#include <iostream>
#include <numeric>

using namespace std;

int solve(int M, int N, int x, int y) {
    int last = M * N / gcd(M, N);
    int a = x, b = y;
    while (a != b) {
            if (a > b) b += N;
            else a += M;
            if (a > last || b > last) return -1;
        }
    return a;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int M, N, x, y;
        cin >> M >> N >> x >> y;
        int result = solve(M, N, x, y);
        cout << result << "\n"; 
    }
    return 0;
}