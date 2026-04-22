#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    n--;

    int baseCode = 0xAC00;
    int unicode = baseCode + n;

    string utf8_char = "";
    utf8_char += (char)(0xE0 | (unicode >> 12));
    utf8_char += (char)(0x80 | ((unicode >> 6) & 0x3F));
    utf8_char += (char)(0x80 | (unicode & 0x3F));

    cout << utf8_char << endl;

    return 0;
}