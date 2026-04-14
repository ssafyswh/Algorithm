#include <iostream>
#include <vector>

using namespace std;

vector<int> info;

int find(int user) {
    if (info[user] == user) return user;
    return info[user] = find(info[user]);
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    info[b] = a;
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    for (int t = 1; t < T + 1; t++) {
        int n, k;
        cin >> n >> k;
        info.clear();
        for (int i = 0; i < n; i++) info.push_back(i);
        for (int i = 0; i < k; i++) {
            int a, b;
            cin >> a >> b;
            unite(a, b);
        }
        
        int m;
        cin >> m;
        cout << "Scenario " << t << ":\n";
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            if (find(u) == find(v)) cout << 1;
            else cout << 0;
            cout << "\n";
        }
        cout << "\n" ;
    }
    return 0; 
}