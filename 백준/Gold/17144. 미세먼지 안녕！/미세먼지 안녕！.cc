#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int R, C, T;

vector<pair<int, int>> delta = {
    {0, 1},
    {1, 0},
    {0, -1},
    {-1, 0},
};

bool check(int r, int c) {
    if (r < 0 || r >= R) return false;
    if (c < 0 || c >= C) return false;
    return true;
}

vector<vector<int>> room;

void spread_dust() {
    vector<vector<int>> diff(R, vector<int>(C, 0));
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            int dust = room[r][c];
            int spread = dust / 5;
            for (pair<int ,int> d : delta) {
                int nr = r + d.first, nc = c + d.second;
                if (check(nr, nc) && room[nr][nc] != -1) {
                    diff[nr][nc] += spread;
                    diff[r][c] -= spread;
                }
            }
        }
    }
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            room[r][c] += diff[r][c];
        }
    }
}

void purify(int sr, int sc, bool is_clockwise) {
    if (is_clockwise) {
        room[sr + 1][sc] = 0;
        for (int r = sr + 1; r < R - 1; r++) {
            swap(room[r][sc], room[r + 1][sc]);
        }
        for (int c = sc; c < C - 1; c++) {
            swap(room[R - 1][c], room[R - 1][c + 1]);
        }
        for (int r = R - 1; r > sr; r--) {
            swap(room[r][C - 1], room[r - 1][C - 1]);
        }
        for (int c = C - 1; c > sc + 1; c--) {
            swap(room[sr][c], room[sr][c - 1]);
        }
    }
    else {
        room[sr - 1][sc] = 0;
        for (int r = sr - 1; r > 0; r--) {
            swap(room[r][sc], room[r - 1][sc]);
        }
        for (int c = sc; c < C - 1; c++) {
            swap(room[0][c], room[0][c + 1]);
        }
        for (int r = 0; r < sr; r++) {
            swap(room[r][C - 1], room[r + 1][C - 1]);
        }
        for (int c = C - 1; c > sc + 1; c--) {
            swap(room[sr][c], room[sr][c - 1]);
        }
    }
}

int result() {
    int value = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            value += room[r][c];
        }
    }
    return value;
}

int main() {
    cin >> R >> C >> T;
    vector<pair<int, int>> purifier;
    for (int y = 0; y < R; y++) {
        room.push_back(vector<int> {});
        for (int x = 0; x < C; x++) {
            int dust;
            cin >> dust;
            if (dust == -1) {
                purifier.push_back({y, x});
            }
            room[y].push_back(dust);
        }
    }
    pair<int, int> p1 = purifier[0], p2 = purifier[1];

    while (T--) {
        spread_dust();
        purify(p1.first, p1.second, false);
        purify(p2.first, p2.second, true);
    }
    cout << result() + 2;
    return 0;
}