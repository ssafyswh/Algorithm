#include <iostream>

using namespace std;

int main() {
    int a, i;
    if (cin >> a >> i) {
        int result = a * (i - 1) + 1;
        cout << result << endl;
    }

    return 0;
}