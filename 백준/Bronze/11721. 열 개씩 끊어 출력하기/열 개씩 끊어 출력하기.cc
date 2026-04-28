#include <iostream>
#include <string>

int main() {
    std::string s;
    std::cin >> s;

    for (int i = 0; i < s.length(); i++) {
        std::cout << s[i];
        if ((i + 1) % 10 == 0) {
            std::cout << std::endl;
        }
    }

    if (s.length() % 10 != 0) {
        std::cout << std::endl;
    }

    return 0;
}