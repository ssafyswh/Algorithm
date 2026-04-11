#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n, s;
    cin >> n >> s;
    int m;
    cin >> m;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    vector<int> consume(m + 1, 0);
    for (int i = 1; i < m + 1; i++) {
        cin >> consume[i];
        pq.push({0, i});
    }
    int result = 0;
    for (int i = 0; i < n - s; i++) {
        long long time = pq.top().first;
        int num = pq.top().second;
        result = num;
        pq.pop();
        pq.push({time + consume[num], num});
    }
    cout << result;
    return 0; 
}