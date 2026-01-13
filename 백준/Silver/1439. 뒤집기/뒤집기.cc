#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int len = s.length();
    int zero = 0, one = 0;
    if (s[0] == '0') zero++;
    else one++;
    for (int i = 1; i < len; i++) {
        if (s[i] != s[i - 1]) {
            if (s[i] == '0') zero++;
            else one++;
        }
    }
    int result = min(zero, one);
    cout << result;
    return 0;
}