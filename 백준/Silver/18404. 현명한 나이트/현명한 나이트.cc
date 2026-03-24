#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int deltax[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int deltay[8] = {-1, 1, -2, 2, -2, 2, -1, 1};

struct node {
    int move;
    int y;
    int x;
};

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> board(N, vector<int>(N, 10e8));

    int X, Y;
    cin >> X >> Y;
    board[Y - 1][X - 1] = 0;

    queue<node> q;
    q.push({0, Y - 1, X - 1});
    while (!q.empty()) {
        node now = q.front();
        q.pop();
        for (int i = 0; i < 8; i++) {
            int dy = now.y + deltay[i], dx = now.x + deltax[i];
            if (dy < 0 || dx < 0 || dy >= N || dx >= N) continue;
            if (board[dy][dx] <= now.move + 1) continue;
            q.push({now.move + 1, dy, dx});
            board[dy][dx] = now.move + 1;
        }
    }
    for (int i = 0; i < M; i ++) {
        int A, B;
        cin >> A >> B;
        cout << board[B - 1][A - 1] << " " ;
    }
    return 0;
}