#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        int ord;
        string text;
        cin >> ord >> text;
        text.erase(ord - 1, 1);
        cout << text << "\n";
    }
    return 0;
}