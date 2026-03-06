#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int idx = -1;
        while (n > 0) {
            idx++;
            if (n % 2 == 1) {
                cout << idx << " ";
            }
            n /= 2;
        }
        cout << "\n";
    }
    return 0;
}