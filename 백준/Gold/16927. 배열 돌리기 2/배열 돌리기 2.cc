#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, int> rotate(pair<int, int>pos, int n, int m, int r) {
    int y = pos.first;
    int x = pos.second;
    
    int k = min({y, n - 1 - y, x, m - 1 - x});
    
    int y_min = k, y_max = n - 1 - k;
    int x_min = k, x_max = m - 1 - k;
    
    int H = y_max - y_min;
    int W = x_max - x_min;
    int L = 2 * H + 2 * W;
    
    int idx = 0;
    if (x == x_min && y < y_max) {
        idx = y - y_min;
    } else if (y == y_max && x < x_max) {
        idx = H + (x - x_min);
    } else if (x == x_max && y > y_min) {
        idx = H + W + (y_max - y);
    } else if (y == y_min && x > x_min) {
        idx = 2 * H + W + (x_max - x);
    }
    
    int new_idx = (idx + r) % L;
    
    int new_y, new_x;
    if (new_idx < H) {
        new_y = y_min + new_idx;
        new_x = x_min;
    } else if (new_idx < H + W) {
        new_y = y_max;
        new_x = x_min + (new_idx - H);
    } else if (new_idx < 2 * H + W) {
        new_y = y_max - (new_idx - H - W);
        new_x = x_max;
    } else {
        new_y = y_min;
        new_x = x_max - (new_idx - 2 * H - W);
    }
    
    return {new_y, new_x};
}

int main() {
    int N, M, R;
    cin >> N >> M >> R;
    
    vector<vector<int>> A(N, vector<int>(M));
    vector<vector<int>> Ans(N, vector<int>(M));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> A[i][j];
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            pair<int, int> new_pos = rotate({i, j}, N, M, R);
            Ans[new_pos.first][new_pos.second] = A[i][j];
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << Ans[i][j] << (j == M - 1 ? "" : " ");
        }
        cout << "\n";
    }
    
    return 0; 
}