#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    string max_result;
    string min_result;
    int miny, minm, mind, maxy, maxm, maxd;
    for (int i = 0; i < n; i++)
    {
        string name;
        int d, m, y;
        cin >> name >> d >> m >> y;
        if (i == 0)
        {
            miny = y;
            minm = m;
            mind = d;
            maxy = y;
            maxm = m;
            maxd = d;
            max_result = name;
            min_result = name;
        }
        else
        {
            if (maxy < y)
            {
                maxy = y;
                maxm = m;
                maxd = d;
                max_result = name;
            }
            else if (maxy == y)
            {
                if (maxm < m)
                {
                    maxy = y;
                    maxm = m;
                    maxd = d;
                    max_result = name;
                }
                else if (maxm == m)
                {
                    if (maxd < d)
                    {
                        maxy = y;
                        maxm = m;
                        maxd = d;
                        max_result = name;
                    }
                }
            }
            else
            {
                if (miny > y)
                {
                    miny = y;
                    minm = m;
                    mind = d;
                    min_result = name;
                }
                else if (miny == y)
                {
                    if (minm > m)
                    {
                        miny = y;
                        minm = m;
                        mind = d;
                        min_result = name;
                    }
                    else if (minm == m)
                    {
                        if (mind > d)
                        {
                            miny = y;
                            minm = m;
                            mind = d;
                            min_result = name;
                        }
                    }
                }
            }
        }
    }
    cout << max_result << "\n"
         << min_result;
    return 0;
}