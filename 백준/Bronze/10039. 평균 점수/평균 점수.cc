#include <iostream>

int main()
{
    int total = 0;
    for (int i = 0; i < 5; i++)
    {
        int score;
        std::cin >> score;
        if (score >= 40)
        {
            total += score;
        }
        else
        {
            total += 40;
        };
    };
    int avg = total / 5;
    std::cout << avg;
    return 0;
}