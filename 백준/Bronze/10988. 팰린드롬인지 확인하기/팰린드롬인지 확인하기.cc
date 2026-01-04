#include <iostream>
#include <string>
using namespace std;

bool pelindrome(const string s)
{
    int len = s.length();
    for (int i = 0; i < len / 2; i++)
    {
        if (s[i] != s[len - i - 1])
            return false;
    }
    return true;
}

int main()
{
    string word;
    cin >> word;
    if (pelindrome(word))
    {
        cout << 1;
    }
    else
        cout << 0;
    return 0;
}