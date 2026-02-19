#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include <climits>

using namespace std;

const int MAX = INT_MAX;

int N, K;
int result = MAX;
string series = "", answer = "";
unordered_set<string> memoization;

int main() {
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        answer += to_string(i);
    }

    for (int i = 0; i < N; i++) {
        char element;
        cin >> element;
        series += element;
    }
    memoization.insert(series);

    deque<pair<int, string>> dq = {{0, series}};
    while (!dq.empty()) {
        int cnt = dq.front().first;
        string now = dq.front().second;
        dq.pop_front();
        if (now == answer) {
            result = cnt;
            break;
        }

        for (int i = 0; i <= (N - K); i++) {
            string new_series = now;
            for (int j = 0; j < (K / 2); j++) {
                swap(new_series[i + j], new_series[i + K - 1 - j]);
            }
            if (memoization.count(new_series) != 0) continue;
            memoization.insert(new_series);
            dq.push_back({cnt + 1, new_series});
        }   
    }
    if (result == MAX) cout << -1;
    else cout << result;
    return 0;
}