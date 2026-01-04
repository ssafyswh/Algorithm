#include <iostream>
#include <algorithm>
#include <string>

using std::cin;
using std::cout;

int main()
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int r, e, c;
        cin >> r >> e >> c;
        int profit = e - c - r;
        if (profit > 0) cout << "advertise";
        else if (profit == 0) cout << "does not matter";
        else cout << "do not advertise";
        cout << "\n";
    }
    return 0;
}