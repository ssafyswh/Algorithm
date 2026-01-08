#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{

    int N, M;
    cin >> N >> M;
    vector<int> ward(N, 0);
    for (int i = 0; i < N; i++)
    {
        cin >> ward[i];
    }
    ward[N - 1] = 0;
    vector<vector<pair<int, int>>> lane(N);
    for (int i = 0; i < M; i++)
    {
        int a, b, t;
        cin >> a >> b >> t;
        lane[a].push_back({b, t});
        lane[b].push_back({a, t});
    }
    long long INF = 1e12;
    vector<long long> result(N, INF);
    result[0] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> hq;
    hq.push({0, 0});
    while (!hq.empty())
    {
        long long now_dist = hq.top().first;
        int now_pos = hq.top().second;
        hq.pop();
        if (now_dist > result[now_pos])
            continue;
        if (now_pos == N - 1)
            break;
        for (pair<int, int> target : lane[now_pos])
        {
            int nxt_pos = target.first;
            int dist = target.second;
            if (ward[nxt_pos] == 1)
                continue;
            long long nxt_dist = dist + now_dist;
            if (nxt_dist < result[nxt_pos])
            {
                result[nxt_pos] = nxt_dist;
                hq.push({nxt_dist, nxt_pos});
            }
        }
    }
    if (result[N - 1] != INF)
        cout << result[N - 1];
    else
        cout << -1;

    return 0;
}