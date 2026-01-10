#include <iostream>
#include <vector>

using namespace std;
vector<vector<int>> dp(10004, vector<int>(3, 0));

int main()
{
    dp[1][0] = 1;
    dp[2][1] = 1;
    dp[3][2] = 1;
    for (int i = 1; i <= 10000; i++) {
        dp[i + 1][0] = dp[i][2] + dp[i][1] + dp[i][0];
        dp[i + 2][1] = dp[i][2] + dp[i][1];
        dp[i + 3][2] = dp[i][2];
    }
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        int n;
        cin >> n;
        int result = dp[n][2] + dp[n][1] + dp[n][0];
        cout << result << "\n";
    }
    return 0;
}