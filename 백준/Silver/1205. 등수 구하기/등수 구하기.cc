#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, new_score, P;
    cin >> N >> new_score >> P;

    if (N == 0)
    {
        cout << 1;
        return 0;
    }

    vector<int> scores(N);
    for (int i = 0; i < N; i++)
    {
        cin >> scores[i];
    }
    if (N == P && scores[N - 1] >= new_score)
    {
        cout << -1;
        return 0;
    }
    int rank = 1;
    for (int i = 0; i < N; i++)
    {
        if (scores[i] > new_score)
            rank++;
        else
            break;
    }
    cout << rank;
    return 0;
}