#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> schedules(N);
    for (int i = 0; i < N; i++) {
        cin >> schedules[i].first >> schedules[i].second;
    }
    sort(schedules.begin(), schedules.end());

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < N; i++) {
        int start = schedules[i].first;
        int end = schedules[i].second;
        if (!pq.empty() && pq.top() <= start) {
            pq.pop(); 
        }
        pq.push(end);
    }
    cout << pq.size();
    return 0;
}