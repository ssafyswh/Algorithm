#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};
vector<vector<int>> forest, dp;

int route(int y, int x)
{
    if (dp[y][x] != 0)
        return dp[y][x];
    dp[y][x] = 1;
    int bamboo = forest[y][x];
    for (int i = 0; i < 4; i++)
    {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (!(0 <= ny && ny < N && 0 <= nx && nx < N))
            continue;
        if (bamboo < forest[ny][nx])
        {
            dp[y][x] = max({route(ny, nx) + 1, dp[y][x]});
        }
    }
    return dp[y][x];
}

int main()
{
    cin >> N;
    forest.assign(N, vector<int>(N));
    dp.assign(N, vector<int>(N, 0));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> forest[i][j];
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (dp[i][j] == 0)
            {
                route(i, j);
            }
        }
    }
    int result = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (result < dp[i][j])
                result = dp[i][j];
        }
    }
    cout << result;
    return 0;
}