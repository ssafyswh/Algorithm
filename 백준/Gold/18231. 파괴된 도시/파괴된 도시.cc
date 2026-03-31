#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<int>> roads(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        roads[u].push_back(v);
        roads[v].push_back(u);
    }

    int K;
    cin >> K;
    
    vector<bool> is_target(N + 1, false);
    for (int i = 0; i < K; i++) {
        int p;
        cin >> p;
        is_target[p] = true;
    }

    vector<int> bomb_candidates;
    for (int i = 1; i <= N; i++) {
        if (!is_target[i]) continue;
        
        bool can_plant = true;
        for (int neighbor : roads[i]) {
            if (!is_target[neighbor]) {
                can_plant = false;
                break;
            }
        }
        
        if (can_plant) {
            bomb_candidates.push_back(i);
        }
    }

    vector<bool> actually_destroyed(N + 1, false);
    for (int bomb_city : bomb_candidates) {
        actually_destroyed[bomb_city] = true;
        for (int neighbor : roads[bomb_city]) {
            actually_destroyed[neighbor] = true;
        }
    }

    bool possible = true;
    for (int i = 1; i <= N; i++) {
        if (is_target[i] != actually_destroyed[i]) {
            possible = false;
            break;
        }
    }

    if (!possible) {
        cout << -1 << "\n";
    } else {
        cout << bomb_candidates.size() << "\n";
        for (int i = 0; i < bomb_candidates.size(); i++) {
            cout << bomb_candidates[i] << (i == bomb_candidates.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}