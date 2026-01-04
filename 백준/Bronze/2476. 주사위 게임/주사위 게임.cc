#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;

int main()
{
    int N;
    cin >> N;
    int result = 0;
    for (int i = 0; i < N; i++) {
        int a, b, c, prize;
        cin >> a >> b >> c;
        if (a == b && b == c) prize = a * 1000 + 10000;
        else if (a == b) prize = a * 100 + 1000;
        else if (b == c) prize = b * 100 + 1000;
        else if (c == a) prize = c * 100 + 1000;
        else prize = std::max({a, b, c}) * 100;
        if (result < prize) result = prize;
    }
    cout << result;
    return 0;
}