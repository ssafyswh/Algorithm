#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct State {
    int r, c, used;
};

int n, m;
long long board[100][100];
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

bool can_escape(long long limit) {
    if (board[0][0] > limit) return false;

    vector<vector<vector<bool>>> visited(n, vector<vector<bool>>(m, vector<bool>(2, false)));
    queue<State> q;

    q.push({0, 0, 0});
    visited[0][0][0] = true;

    while (!q.empty()) {
        State cur = q.front();
        q.pop();

        if (cur.r == n - 1 && cur.c == m - 1) return true;

        for (int i = 0; i < 4; i++) {
            int nr = cur.r + dr[i];
            int nc = cur.c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                if (board[nr][nc] <= limit && !visited[nr][nc][cur.used]) {
                    visited[nr][nc][cur.used] = true;
                    q.push({nr, nc, cur.used});
                }
            }

            if (cur.used == 0) {
                int nnr = cur.r + dr[i] * 2;
                int nnc = cur.c + dc[i] * 2;

                if (nnr >= 0 && nnr < n && nnc >= 0 && nnc < m) {
                    if (board[nnr][nnc] <= limit && !visited[nnr][nnc][1]) {
                        visited[nnr][nnc][1] = true;
                        q.push({nnr, nnc, 1});
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    cin >> n >> m;
    long long low = 0, high = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
            high = max(high, board[i][j]);
        }
    }

    long long ans = high;
    while (low <= high) {
        long long mid = (low + high) / 2;
        if (can_escape(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << endl;

    return 0;
}