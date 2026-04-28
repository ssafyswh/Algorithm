#include <iostream>

using std::cin;
using std::cout;

int main()
{
    int N;
    cin >> N;
    int res = 0;
    for (int i = 0; i < N; i++)
    {
        int cute;
        cin >> cute;
        if (cute == 1)
            res++;
    }
    if (res > N / 2) cout << "Junhee is cute!";
    else cout << "Junhee is not cute!";
    return 0;
}