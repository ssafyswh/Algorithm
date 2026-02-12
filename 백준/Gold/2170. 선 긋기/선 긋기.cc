#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    vector<pair<long long, long long>> lines(N, {0, 0});
    for (int i = 0; i < N; i++) {
        cin >> lines[i].first;
        cin >> lines[i].second;
    }
    sort(lines.begin(), lines.end());
    long long start = lines[0].first, finish = lines[0].second;
    long long result = finish - start;
    for (int i = 1; i < N; i++) {
        long long nxt_start = lines[i].first, nxt_finish = lines[i].second;
        if (nxt_finish <= finish) continue;
        else if (nxt_start <= finish && nxt_finish > finish) {
            result += nxt_finish - finish;
            finish = nxt_finish;
        } else {
            result += nxt_finish - nxt_start;
            start = nxt_start;
            finish = nxt_finish;
        }
    }
    cout << result;
    return 0;
}