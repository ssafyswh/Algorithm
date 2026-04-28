#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> visited(100001, -1);

bool is_valid(int pos, int move) {
    if (pos >= 0 && pos <= 100000 && (visited[pos] == -1 || visited[pos] > move) ) return true;
    return false;
}

int main() {
    int A, B, N, M;
    cin >> A >> B >> N >> M;
    queue<pair<int, int>> q;
    q.push({0, N});
    while (!q.empty()) {
        int move = q.front().first, pos = q.front().second;
        if (pos == M) {
            cout << move;
            break;
        }
        q.pop();
        if (is_valid(pos - 1, move + 1)) {
            q.push({move + 1, pos - 1});
            visited[pos - 1] = move + 1;
        }
        if (is_valid(pos + 1, move + 1)) {
            q.push({move + 1, pos + 1});
            visited[pos + 1] = move + 1;
        }
        if (is_valid(pos - A, move + 1)) {
            q.push({move + 1, pos - A});
            visited[pos - A] = move + 1;
        }
        if (is_valid(pos + A, move + 1)) {
            q.push({move + 1, pos + A});
            visited[pos + A] = move + 1;
        }
        if (is_valid(pos - B, move + 1)) {
            q.push({move + 1, pos - B});
            visited[pos - B] = move + 1;
        }
        if (is_valid(pos + B, move + 1)) {
            q.push({move + 1, pos + B});
            visited[pos + B] = move + 1;
        }
        if (is_valid(pos * A, move + 1)) {
            q.push({move + 1, pos * A});
            visited[pos * A] = move + 1;
        }
        if (is_valid(pos * B, move + 1)) {
            q.push({move + 1, pos * B});
            visited[pos * B] = move + 1;
        }
    }
    return 0;
}