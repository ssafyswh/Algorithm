#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void solve()
{
    int N;
    cin >> N;
    vector<int> race(N);
    unordered_map<int, int> team_size;

    for (int i = 0; i < N; i++)
    {
        cin >> race[i];
        team_size[race[i]]++;
    }

    // tema info: count, sum_score, fifth
    unordered_map<int, vector<int>> team_info;
    int current_rank = 1;

    for (int i = 0; i < N; i++)
    {
        int id = race[i];
        if (team_size[id] < 6)
            continue;

        if (team_info[id].empty())
            team_info[id] = {0, 0, 0};

        team_info[id][0]++;
        if (team_info[id][0] <= 4)
        {
            team_info[id][1] += current_rank;
        }
        else if (team_info[id][0] == 5)
        {
            team_info[id][2] = current_rank;
        }
        current_rank++;
    }

    int winner = -1;
    int min_sum = 1e9;
    int min_fifth = 1e9;

    for (auto const &[id, data] : team_info)
    {
        int cur_sum = data[1];
        int cur_fifth = data[2];

        if (cur_sum < min_sum)
        {
            min_sum = cur_sum;
            min_fifth = cur_fifth;
            winner = id;
        }
        else if (cur_sum == min_sum)
        {
            if (cur_fifth < min_fifth)
            {
                min_fifth = cur_fifth;
                winner = id;
            }
        }
    }
    cout << winner << "\n";
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        solve();
    }
    return 0;
}