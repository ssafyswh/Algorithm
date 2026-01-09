#include <iostream>

using namespace std;

int combi[31][31] = {0};

int main() {
    combi[0][0] = 1;
    for (int i = 1; i <= 30; i ++) {
        for (int j = 0; j <= i; j++) {
            combi[i][j] = combi[i - 1][j - 1] + combi[i - 1][j];
        }
    }
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, m;
        cin >> n >> m;
        cout << combi[m][n] << "\n";
    }
    return 0;
}