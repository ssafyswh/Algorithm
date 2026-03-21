#include <iostream>
#include <algorithm>

using namespace std;

int n, m, k;
int laptop[45][45];
int sticker[15][15];

bool can_attach(int x, int y, int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (laptop[x + i][y + j] == 1 && sticker[i][j] == 1) {
                return false;
            }
        }
    }
    return true;
}

void attach(int x, int y, int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (sticker[i][j] == 1) {
                laptop[x + i][y + j] = 1;
            }
        }
    }
}

void rotate(int& r, int& c) {
    int temp[15][15];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            temp[j][r - 1 - i] = sticker[i][j];
        }
    }

    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            sticker[i][j] = temp[i][j];
        }
    }
    swap(r, c);
}

int main() {
    cin >> n >> m >> k;

    while (k--) {
        int r, c;
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> sticker[i][j];
            }
        }
        bool attached = false;
        for (int rot = 0; rot < 4; rot++) {
            for (int i = 0; i <= n - r; i++) {
                for (int j = 0; j <= m - c; j++) {
                    if (can_attach(i, j, r, c)) {
                        attach(i, j, r, c);
                        attached = true;
                        break;
                    }
                }
                if (attached) break;
            }
            if (attached) break;
            rotate(r, c);
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            ans += laptop[i][j];
        }
    }

    cout << ans << '\n';

    return 0;
}