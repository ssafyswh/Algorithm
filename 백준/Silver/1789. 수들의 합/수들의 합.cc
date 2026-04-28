#include <iostream>
#include <cmath>

int main()
{
    long long S;
    std::cin >> S;
    double maximum;
    maximum = (sqrt(1 + 8 * S) - 1) / 2;
    std::cout << std::floor(maximum);

    return 0;
}