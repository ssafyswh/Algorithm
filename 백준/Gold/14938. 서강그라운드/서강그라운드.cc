#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int INF = 300000;

int main()
{
    int n, m, r;
    cin >> n >> m >> r;
    vector<int> items(n + 1);
    for (int i = 1; i < n + 1; i++)
    {
        cin >> items[i];
    }
    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    vector<vector<pair<int, int>>> edges(n + 1);
    for (int i = 1; i < n + 1; i++)
    {
        dist[i][i] = 0;
    }
    for (int i = 0; i < r; i++)
    {
        int a, b, l;
        cin >> a >> b >> l;
        edges[a].push_back({l, b});
        edges[b].push_back({l, a});
        dist[a][b] = l;
        dist[b][a] = l;
    }
    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < n + 1; j++)
        {
            for (int k = 1; k < n + 1; k++)
            {
                if (dist[j][k] > dist[j][i] + dist[i][k])
                {
                    dist[j][k] = dist[j][i] + dist[i][k];
                }
            }
        }
    }
    vector<int> result(n + 1, 0);
    for (int i = 0; i < n + 1; i++)
    {
        for (int j = 0; j < n + 1; j++)
        {
            if (dist[i][j] <= m)
                result[i] += items[j];
        }
    }
    int ans = *max_element(result.begin(), result.end());
    cout << ans;
    return 0;
}