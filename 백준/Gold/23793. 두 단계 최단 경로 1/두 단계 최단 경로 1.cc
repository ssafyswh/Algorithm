#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;
int N, M;
vector<vector<pair<int, long long>>> edges;

long long dijkstra(int start, int end, int avoid) {
    vector<long long> dist(N + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        long long current_dist = pq.top().first;
        int current_node = pq.top().second;
        pq.pop();
        if (current_dist > dist[current_node]) continue;
        for (auto& edge : edges[current_node]) {
            int next_node = edge.first;
            long long weight = edge.second;
            if (next_node == avoid) continue;
            if (dist[current_node] + weight < dist[next_node]) {
                dist[next_node] = dist[current_node] + weight;
                pq.push({dist[next_node], next_node});
            }
        }
    }

    return dist[end];
}

int main() {
    cin >> N >> M;
    edges.resize(N + 1);

    for (int i = 0; i < M; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        edges[u].push_back({v, w});
    }

    int x, y, z;
    cin >> x >> y >> z;
    long long dist_x_to_y = dijkstra(x, y, -1);
    long long dist_y_to_z = dijkstra(y, z, -1);
    long long answer1 = -1;
    if (dist_x_to_y != INF && dist_y_to_z != INF) {
        answer1 = dist_x_to_y + dist_y_to_z;
    }
    long long dist_x_to_z_without_y = dijkstra(x, z, y);
    long long answer2 = -1;
    if (dist_x_to_z_without_y != INF) {
        answer2 = dist_x_to_z_without_y;
    }
    cout << answer1 << " " << answer2 << "\n";
    return 0;
}