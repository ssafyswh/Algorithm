#include <iostream>
#include <string>
using namespace std;

int main()
{
    string start, fin;
    cin >> start >> fin;
    int start_time, fin_time;
    start_time = (int(start[0]) * 10 + int(start[1])) * 3600 + (int(start[3]) * 10 + int(start[4])) * 60 + (int(start[6]) * 10 + int(start[7]));
    fin_time = (int(fin[0]) * 10 + int(fin[1])) * 3600 + (int(fin[3]) * 10 + int(fin[4])) * 60 + (int(fin[6]) * 10 + int(fin[7]));
    int res;
    res = fin_time - start_time;
    if (res < 0)
        res = 86400 + res;
    int h, m, s;
    h = res / 3600;
    m = (res - 3600 * h) / 60;
    s = res - 3600 * h - m * 60;
    if (h < 10)
        cout << 0;
    cout << h << ":";
    if (m < 10)
        cout << 0;
    cout << m << ":";
    if (s < 10)
        cout << 0;
    cout << s;
    return 0;
}