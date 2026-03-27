#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<long long>> backroom(N, vector<long long>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) cin >> backroom[i][j];
    }

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    if (x1 > x2) swap(x1, x2);
    if (y1 > y2) swap(y1, y2);

    vector<vector<long long>> dp(N, vector<long long>(M, -INF));
    dp[0][0] = backroom[0][0];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (dp[i][j] == -INF) continue;

            if (j + 1 < M) {
                bool blocked = false;
                if (y1 == y2 && y1 == j + 1 && x1 <= i && i < x2) {
                    blocked = true;
                }
                if (!blocked) {
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + backroom[i][j + 1]);
                }
            }

            if (i + 1 < N) {
                bool blocked = false;
                if (x1 == x2 && x1 == i + 1 && y1 <= j && j < y2) {
                    blocked = true;
                }
                if (!blocked) {
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + backroom[i + 1][j]);
                }
            }
        }
    }

    if (dp[N - 1][M - 1] <= -INF / 2) cout << "Entity\n";
    else cout << dp[N - 1][M - 1] << "\n";

    return 0;
}