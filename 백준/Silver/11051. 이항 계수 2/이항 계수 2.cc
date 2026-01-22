#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<vector<int>> pascal(N + 1, vector<int>(N + 1));
    for (int i = 0; i < N + 1; i++) {
        pascal[i][0] = 1;
        for (int j = 1; j < i; j++) {
            pascal[i][j] = (pascal[i - 1][j - 1] + pascal[i - 1][j]) % 10007;
        }
        pascal[i][i] = 1;
    }
    cout << pascal[N][K] % 10007;
    return 0;
}