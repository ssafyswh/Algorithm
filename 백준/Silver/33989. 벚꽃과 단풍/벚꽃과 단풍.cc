#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int N;
    string S;
    cin >> N >> S;
    vector<int> result(N + 1, 0);
    int cnt_d = 0, cnt_b = 0;
    for (int i = 1; i < N + 1; i++)
    {
        if (S[i - 1] == 'D')
        {
            cnt_d++;
        }
        result[i] += cnt_d;
    }
    for (int j = N; j >= 0; j--)
    {
        if (S[j] == 'B')
        {
            cnt_b++;
        }
        result[j] += cnt_b;
    }
    auto res = min_element(result.begin(), result.end());
    cout << *res;
    return 0;
}