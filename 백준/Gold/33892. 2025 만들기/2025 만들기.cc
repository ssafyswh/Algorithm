#include <iostream>
#include <string>

using namespace std;

string odd = "YES\n6 * 7\n42 + 3\n4 * 2\n8 + 1\n9 * 5\n45 * 45\n";
string even = "YES\n6 * 7\n42 + 3\n8 * 5\n40 + 4\n44 + 2\n46 - 1\n45 * 45\n";

int main() {
    int N;
    cin >> N;
    if (N <= 6) {
        cout << "NO";
        return 0;
    }
    if (N % 2 == 1) {
        cout << odd;
        for (int i = 0; i < (N - 7) / 2; i++) {
            cout << 9 + 2 * i << " - " << 8 + 2 * i << "\n";
            cout << "2025 * 1\n";
        }
    } else {
        cout << even;
        for (int i = 0; i < (N - 8) / 2; i++) {
            cout << 10 + 2 * i << " - " << 9 + 2 * i << "\n";
            cout << "2025 * 1\n";
        }
    }
    return 0;
}