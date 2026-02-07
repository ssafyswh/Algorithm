#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N, L;
int map[100][100];

bool check(vector<int>& line) {
    int cnt = 1;
    for (int i = 0; i < N - 1; i++) {
        if (line[i] == line[i + 1]) {
            cnt++;
        } else if (line[i] + 1 == line[i + 1]) {
            if (cnt >= L) {
                cnt = 1;
            } else {
                return false;
            }
        } else if (line[i] - 1 == line[i + 1]) {
            if (i + L >= N) return false;
            for (int j = 1; j <= L; j++) {
                if (line[i + 1] != line[i + j]) return false;
            }
            i += L - 1;
            cnt = 0;
        } else {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> L;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
        }
    }
    int result = 0;
    for (int i = 0; i < N; i++) {
        vector<int> line;
        for (int j = 0; j < N; j++) line.push_back(map[i][j]);
        if (check(line)) result++;
    }

    for (int j = 0; j < N; j++) {
        vector<int> line;
        for (int i = 0; i < N; i++) line.push_back(map[i][j]);
        if (check(line)) result++;
    }

    cout << result;

    return 0;
}