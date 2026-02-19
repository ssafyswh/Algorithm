#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> lectures(N);
    for (int i = 0; i < N; i++) {
        int n, start, finish;
        cin >> n >> start >> finish;
        lectures[i] = {start, finish};
    }
    sort(lectures.begin(), lectures.end());

    priority_queue<int, vector<int>, greater<int>> room;
    for (int i = 0; i < N; i++) {
        if (room.empty()) {
            room.push(lectures[i].second);
            continue;
        }
        if (room.top() <= lectures[i].first) {
            room.pop();
        } 
        room.push(lectures[i].second);
    }
    cout << room.size();
    return 0;   
}