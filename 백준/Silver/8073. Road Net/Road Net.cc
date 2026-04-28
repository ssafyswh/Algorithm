#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> dist(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> dist[i][j];
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            bool is_neighbor = true;
            for (int k = 1; k <= n; ++k) {
                if (k == i || k == j) continue;
                if (dist[i][j] == dist[i][k] + dist[k][j]) {
                    is_neighbor = false;
                    break;
                }
            }
            if (is_neighbor) {
                cout << i << " " << j << "\n";
            }
        }
    }
    return 0;
}