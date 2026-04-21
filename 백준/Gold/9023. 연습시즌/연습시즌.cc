#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

void solve() {
    int C, D, d;
    cin >> C >> D >> d;

    vector<int> X, Y;
    int val;
    while (cin >> val && val != 0) X.push_back(val);
    while (cin >> val && val != 0) Y.push_back(val);

    int n = X.size();
    int m = Y.size();
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(m + 1, vector<int>(3, INF)));
    dp[0][0][0] = 0;

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            if (i == 0 && j == 0) continue;
            if (i > 0 && j > 0) {
                int match_cost;
                if (X[i - 1] == Y[j - 1]) {
                    match_cost = C;
                } else {
                    match_cost = 2 * C;
                }
                dp[i][j][0] = match_cost + min({dp[i - 1][j - 1][0], dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]});
            }

            if (i > 0) {
                int prev_state0 = INF;
                int prev_state1 = INF;
                int prev_state2 = INF;

                if (dp[i - 1][j][0] != INF) prev_state0 = dp[i - 1][j][0] + D + d;
                if (dp[i - 1][j][1] != INF) prev_state1 = dp[i - 1][j][1] + d;
                if (dp[i - 1][j][2] != INF) prev_state2 = dp[i - 1][j][2] + D + d;

                dp[i][j][1] = C + min({prev_state0, prev_state1, prev_state2});
            }
            if (j > 0) {
                int prev_state0 = INF;
                int prev_state1 = INF;
                int prev_state2 = INF;

                if (dp[i][j - 1][0] != INF) prev_state0 = dp[i][j - 1][0] + D + d;
                if (dp[i][j - 1][1] != INF) prev_state1 = dp[i][j - 1][1] + D + d;
                if (dp[i][j - 1][2] != INF) prev_state2 = dp[i][j - 1][2] + d;

                dp[i][j][2] = C + min({prev_state0, prev_state1, prev_state2});
            }
        }
    }
    cout << min({dp[n][m][0], dp[n][m][1], dp[n][m][2]}) << "\n";
}

int main() {
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}