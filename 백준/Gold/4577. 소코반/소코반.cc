#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<char, pair<int, int>> direct = {
    {'U', {-1, 0}},
    {'D', {1, 0}},
    {'L', {0, -1}},
    {'R', {0, 1}},
};

unordered_map<char, char> move_char = {
    {'w', '.'},
    {'W', '+'},
    {'.', 'w'},
    {'+', 'W'},
    {'b', 'w'},
    {'B', 'W'},
};

unordered_map<char, char> move_box = {
    {'b', '.'},
    {'B', '+'},
    {'.', 'b'},
    {'+', 'B'},
};

int main() {
    int T = 0;
    while (true) {
        T++;
        int R, C;
        cin >> R >> C;
        vector<string> map(R);
        if (R == 0 && C == 0) break;
        int box = 0, ny, nx;
        for (int i = 0; i < R; i++) {
            cin >> map[i];
            for (int j = 0; j < C; j++) {
                char tile = map[i][j];
                if (tile == 'w' || tile == 'W') {
                    ny = i; nx = j;
                }
                if (tile == 'b') box++;
            }
        }
        string commands;
        cin >> commands;
        for (int i = 0; i < commands.length(); i++) {
            char command = commands[i];
            pair<int, int> d = direct[command];
            int dy = d.first, dx = d.second;
            int nxt_y = ny + dy, nxt_x = nx + dx;
            char target = map[nxt_y][nxt_x];
            if (target == '#') continue;
            if (target == '.' || target == '+') {
                map[ny][nx] = move_char[map[ny][nx]];
                map[nxt_y][nxt_x] = move_char[target];
                ny = nxt_y; nx = nxt_x;
            } else if (target == 'B' || target == 'b') {
                char move_box_tile = map[nxt_y + dy][nxt_x+dx];
                if (move_box_tile == '.' || move_box_tile == '+') {
                    if (target == 'b' && move_box_tile == '+') box--;
                    else if (target == 'B' && move_box_tile == '.') box++;
                    map[ny][nx] = move_char[map[ny][nx]];
                    map[nxt_y][nxt_x] = move_char[target];
                    map[nxt_y + dy][nxt_x+dx] = move_box[move_box_tile];
                    ny = nxt_y; nx = nxt_x;
                } else continue;
            }

            if (box == 0) break;
        }
        cout << "Game " << T << ": ";
        if (box == 0) cout << "complete";
        else cout << "incomplete";
        cout << "\n";
        for (int i = 0; i < R; i++) {
            cout << map[i] << "\n";
        }
    }
    return 0;
}