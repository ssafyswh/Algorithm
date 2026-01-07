#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<string> room(N);
    for (int i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        room[i] = line;
    }
    int hori = 0;
    for (int y = 0; y < N; y++)
    {
        int cnt_h = 0;
        for (int x = 0; x < N; x++)
        {
            if (room[y][x] == '.')
            {
                cnt_h += 1;
            }
            else
            {
                if (cnt_h >= 2)
                {
                    hori += 1;
                }
                cnt_h = 0;
            }
        }
        if (cnt_h >= 2)
        {
            hori += 1;
        }
    }

    int vert = 0;
    for (int x = 0; x < N; x++)
    {
        int cnt_v = 0;
        for (int y = 0; y < N; y++)
        {
            if (room[y][x] == '.')
            {
                cnt_v += 1;
            }
            else
            {
                if (cnt_v >= 2)
                {
                    vert += 1;
                }
                cnt_v = 0;
            }
        }
        if (cnt_v >= 2)
        {
            vert += 1;
        }
    }
    cout << hori << " " << vert;
    return 0;
}