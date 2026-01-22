#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> dp(K + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= N; i++) {
        for (int j = min(i, K); j > 0; j--) {
            dp[j] = (dp[j] + dp[j - 1]) % 10007;
        }
    }
    cout << dp[K];
    return 0;
}