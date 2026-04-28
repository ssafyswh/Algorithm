#include <iostream>
#include <algorithm>
#include <string>

using std::cin;
using std::cout;

int main()
{
    std::string bowls;
    cin >> bowls;
    int height = 0;
    char top;
    for (int i = 0; i < bowls.length(); i++) {
        char bowl = bowls[i];
        if (i == 0) height += 10;
        else if (bowl == top) height += 5;
        else height += 10;
        top = bowl;
    }
    cout << height;
    return 0;
}