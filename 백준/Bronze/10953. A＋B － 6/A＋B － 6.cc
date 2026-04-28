#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    while(N --) {
        string input;
        cin >> input;
        char a = input[0];
        char b = input[2];
        cout << a + b - '0' - '0' << "\n";
    }
    return 0;
}