#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> edges(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
    int a, b, x;
    cin >> a >> b >> x;
    vector<bool> visited(N + 1, false);

    queue<int> q;
    if (a != x) q.push(a);
    if (b != x) q.push(b);
    visited[a] = true;
    visited[b] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int target : edges[node]) {
            if (visited[target]) continue;
            visited[target] = true;
            if (target != x) q.push(target);
        }
    }

    int result = 1;
    for (int i = 1; i < N + 1; i++) {
        if (!visited[i]) result++;
    }
    cout << result;
    return 0; 
}