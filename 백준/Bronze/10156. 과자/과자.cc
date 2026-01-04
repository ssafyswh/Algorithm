#include <iostream>

using std::cin;
using std::cout;

int main()
{
    int K, N, M;
    cin >> K >> N >> M;
    int budget = K * N - M;
    if (budget >= 0) {
        cout << budget;
    } else {
        cout << 0;
    }
    return 0;
}