#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    pair<int, int> result = {-1, 10e7};
    for (int i = 1; i < n + 1; i++) {
        int j, m;
        cin >> j >> m;
        j -= (j - 1) % (m + 1);
        int turn = 2 + (j / (m + 1)) * 2;
        if (turn < result.second) result = {i, turn};
    }
    cout << result.first << " " << result.second;
    return 0;
}