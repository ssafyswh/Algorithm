#include <iostream>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;

    int t;
    std::cin >> t;

    c += t;

    b += c / 60;
    c %= 60;

    a += b / 60;
    b %= 60;

    a %= 24;

    std::cout << a << " " << b << " " << c << std::endl;

    return 0;
}