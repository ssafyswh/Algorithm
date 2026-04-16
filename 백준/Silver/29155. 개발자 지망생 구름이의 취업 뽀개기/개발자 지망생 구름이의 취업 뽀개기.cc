#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> n(6);
    for (int i = 1; i < 6; i++) cin >> n[i];
    vector<priority_queue<int, vector<int>, greater<>>> pq(6);
    for (int i = 0; i < N; i++) {
        int k, t;
        cin >> k >> t;
        pq[k].push(t);
    }
    int result = 0;
    for (int i = 1; i < 6; i++) {
        int prev = 0;
        for (int j = 0; j < n[i]; j++) {
            if (j == 0) {
                prev = pq[i].top();
                result += prev;
                pq[i].pop();
                continue;
            }
            result += pq[i].top() * 2 - prev;
            prev = pq[i].top();
            pq[i].pop();
        }
        if (i != 5) result += 60;
    }
    cout << result;
    return 0; 
}