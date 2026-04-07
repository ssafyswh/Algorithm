#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

map<int, vector<pair<int, int>>> roads;
int N = 0;

pair<int, int> bfs(int start) {
    queue<pair<int, int>> q;
    vector<bool> visited(N + 1, false);
    int max_dist = 0;
    int farthest_node = start;

    q.push({start, 0});
    visited[start] = true;

    while (!q.empty()) {
        int now = q.front().first;
        int dist = q.front().second;
        q.pop();

        if (dist > max_dist) {
            max_dist = dist;
            farthest_node = now;
        }

        for (pair<int, int> road : roads[now]) {
            if (visited[road.first]) continue;
            visited[road.first] = true;
            q.push({road.first, dist + road.second});
        }
    }
    return {farthest_node, max_dist};
}

int main() {
    int u, v, w;
    bool has_data = false;
    while (cin >> u >> v >> w) {
        has_data = true;
        N = max({u, v, N});
        roads[u].push_back({v, w});
        roads[v].push_back({u, w});
    }

    if (!has_data) {
        cout << 0;
        return 0;
    }
    pair<int, int> first_bfs = bfs(1);
    pair<int, int> second_bfs = bfs(first_bfs.first);

    cout << second_bfs.second << endl;

    return 0;
}