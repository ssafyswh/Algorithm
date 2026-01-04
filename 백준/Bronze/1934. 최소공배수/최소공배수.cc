#include <iostream>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++)
    {
        int A;
        std::cin >> A;
        int B;
        std::cin >> B;
        int res = A * B / gcd(A, B);
        std::cout << res << "\n";
    }
    return 0;
}