#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct edge{
    int weight;
    int start;
    int finish;
};
vector<edge> edges = {{0, 0, 0}};
vector<bool> excluded;
int min_edge = 10001;

class UnionFind {
private:
    vector<int> parent;
    vector<int> sz;

public:
    UnionFind(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) parent[y] = x;
    }
};

int MST(int N, int M) {
    min_edge = 10001;
    vector<int> root(N + 1);
    for (int i = 0; i < N + 1; i++) root[i] = i;
    int cnt = 0, sum = 0;
    UnionFind uf(N);
    for (int i = 1; i < M + 1; i++) {
        if (excluded[i]) continue;
        edge e = edges[i];
        if (min_edge == 10001) {
            min_edge = i;
            uf.unite(e.start, e.finish);
            cnt++;
            sum += e.weight;
        } else {
            if (uf.find(e.start) != uf.find(e.finish)) {
                uf.unite(e.start, e.finish);
                cnt++;
                sum += e.weight;
            }
        }
        if (cnt == N - 1) break;   
    }
    if (cnt < N - 1) return 0;
    excluded[min_edge] = true;
    return sum;
}

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    excluded.resize(M + 1, false);
    for (int i = 1; i < M + 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({i, u, v});
    }

    vector<int> results(K, 0);
    for (int k = 0; k < K; k++) {
        if (k > 0 && results[k - 1] == 0) break;
        results[k] = MST(N, M);
    }
    for (int result : results) cout << result << " ";
    return 0;
}