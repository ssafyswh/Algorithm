#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int W, N;
        cin >> W >> N;
        int result = 0, load = 0, pos = 0;
        for (int i = 0; i < N; i++)
        {
            int x, w;
            cin >> x >> w;
            if (w == 0)
                continue;
            if (load + w < W)
            {
                result += x - pos;
                load += w;
                pos = x;
            }
            else if (load + w == W)
            {
                result += 2 * x - pos;
                load = 0;
                pos = 0;
            }
            else
            {
                result += x - pos;
                pos = x;
                if (w == W)
                {
                    result += 3 * x;
                    pos = 0;
                    load = 0;
                }
                else
                {
                    result += 2 * x;
                    pos = x;
                    load = w;
                }
            }
        }
        result += pos;
        cout << result << "\n";
    }
    return 0;
}